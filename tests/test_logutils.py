import uuid
import logging
import jwt as pyjwt

from terminus import RecordingAdapter
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
