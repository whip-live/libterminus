import logging
import jwt as pyjwt

from terminus import RecordingAdapter


def test_logging_adapter(encoded_jwt):
    """
    Test logging with `recording` argument
    """
    recording = {
        'recording': {
            'device_id': 123,
            'id': 46,
            'jwt': encoded_jwt
        }
    }
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process('test msg', recording)
    expected = ('test msg', {'extra': {'device_id': 123, 'recording_id': 46, 'jwt': 'user'}})
    assert expected == log_result


def test_logging_adapter_topic():
    """
    Test logging with `topic` argument
    """
    topic = {
        'topic': 'test topic'
    }
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process('test msg', topic)
    exepcted = ('test msg', {'extra': {'topic': 'test topic'}})
    assert log_result == exepcted


def test_logging_adapter_jwt(encoded_jwt):
    """
    Test logging with `jwt` argument
    """
    jwt = {
        'jwt': encoded_jwt
    }
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process('test msg', jwt)
    exepcted = ('test msg', {'extra': {'jwt': 'user'}})
    assert log_result == exepcted


def test_logging_adapter_recording_id():
    """
    Test logging with `recording_id` argument
    """
    recording_id = {
        'recording_id': 134
    }
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process('test msg', recording_id)
    exepcted = ('test msg', {'extra': {'recording_id': 134}})
    assert log_result == exepcted


def test_logging_adapter_device_id():
    """
    Test logging with `device_id` argument
    """
    device_id = {
        'device_id': 1
    }
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process('test msg', device_id)
    exepcted = ('test msg', {'extra': {'device_id': 1}})
    assert log_result == exepcted


def test_jwt_without_username():
    data = {
        'email': 'test@test.com',
        'user_id': '123456'
    }
    encoded_jwt = pyjwt.encode(data, '123456', algorithm='HS256')
    jwt = {
        'jwt': encoded_jwt
    }
    logger = logging.getLogger()
    adapter = RecordingAdapter(logger, None)
    log_result = adapter.process('test msg', jwt)
    exepcted = ('test msg', {'extra': {'jwt': '123456'}})
    assert log_result == exepcted
