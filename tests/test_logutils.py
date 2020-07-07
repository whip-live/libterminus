import uuid
import logging
import jwt as pyjwt
import json

from unittest.mock import patch

from terminus import RecordingAdapter, setup_logging
from terminus.proto import recording_pb2


def test_logging_adapter(encoded_jwt):
    """
    Test logging with `recording` argument
    """
    recording_id = uuid.uuid4()
    device_id = uuid.uuid4()
    recording = recording_pb2.Recording()
    recording.id = recording_id.bytes
    recording.device_id = str(device_id)
    recording.jwt = encoded_jwt
    adapter = RecordingAdapter(logging.getLogger(), None)
    log_result = adapter.process("test msg", {"recording": recording})

    expected = (
        "test msg",
        {
            "extra": {
                "device_id": str(device_id),
                "recording_id": str(recording_id),
                "user": "user",
            }
        },
    )
    assert expected == log_result


def test_logging_adapter_topic():
    """
    Test logging with `topic` argument
    """
    topic = {"topic": "test topic"}
    adapter = RecordingAdapter(logging.getLogger(), None)
    log_result = adapter.process("test msg", topic)
    exepcted = ("test msg", {"extra": {"topic": "test topic"}})
    assert log_result == exepcted


def test_logging_adapter_jwt(encoded_jwt):
    """
    Test logging with `jwt` argument
    """
    jwt = {"jwt": encoded_jwt}
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process("test msg", jwt)
    expected = ("test msg", {"extra": {"user": "user"}})
    assert log_result == expected


def test_logging_adapter_recording_id():
    """
    Test logging with `recording_id` argument
    """
    recording_id = {"recording_id": 134}
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process("test msg", recording_id)
    expected = ("test msg", {"extra": {"recording_id": 134}})
    assert log_result == expected


def test_logging_adapter_device_id():
    """
    Test logging with `device_id` argument
    """
    device_id = {"device_id": 1}
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process("test msg", device_id)
    expected = ("test msg", {"extra": {"device_id": 1}})
    assert log_result == expected


def test_jwt_without_username():
    data = {"email": "test@test.com", "user_id": "123456"}
    encoded_jwt = pyjwt.encode(data, "123456", algorithm="HS256")
    jwt = {"jwt": encoded_jwt}
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process("test msg", jwt)
    expected = ("test msg", {"extra": {"user": "123456"}})
    assert log_result == expected


@patch("terminus.logutils.JSONDatagramHandler.send")
def test_loghandler_send_JSON(fake_send, encoded_jwt):
    logger = logging.getLogger(__name__)
    logger = RecordingAdapter(logger, None)

    setup_logging(
        "test_terminus",
        service_level="DEBUG",
        ddagent_host="localhost",
        ddagent_port="10518",
    )
    recording_id = uuid.uuid4()
    device_id = uuid.uuid4()
    recording = recording_pb2.Recording()
    recording.id = recording_id.bytes
    recording.device_id = str(device_id)
    recording.jwt = encoded_jwt

    logger.error("Test log message", recording=recording)

    fake_send.assert_called()
    log_record = json.loads(fake_send.call_args_list[0][0][0].decode())
    assert log_record["levelname"] == "ERROR"
    assert log_record["message"] == "Test log message"
    assert log_record["name"] == "tests.test_logutils"
    assert log_record["service"] == "test_terminus"
    assert log_record["recording_id"] == str(recording_id)
    assert log_record["user"] == "user"
    assert log_record["device_id"] == str(device_id)
