import jwt
import logging

from logging.handlers import DatagramHandler

from pythonjsonlogger import jsonlogger


def get_user_from_jwt(token):
    """
    Decode the JWT to read the payload
    """
    decoded_payload = jwt.decode(token, verify=False, algorithms=['HS256'])
    if 'username' in decoded_payload:
        return decoded_payload['username']
    else:
        return decoded_payload['user_id']


class RecordingAdapter(logging.LoggerAdapter):
    """
    This adapter adds extra fields to a LogRecord
    """

    def process(self, msg, kwargs):
        extra = kwargs.get('extra', {})
        if 'recording' in kwargs:
            extra['device_id'] = kwargs['recording']['device_id']
            extra['recording_id'] = kwargs['recording']['id']
            # add to logging the JWT payload
            extra['jwt'] = get_user_from_jwt(kwargs['recording']['jwt'])

        elif 'topic' in kwargs:
            extra['topic'] = kwargs['topic']
        elif 'device_id' in kwargs:
            extra['device_id'] = kwargs['device_id']
        elif 'recording_id' in kwargs:
            extra['recording_id'] = kwargs['recording_id']
        elif 'jwt' in kwargs:
            extra['jwt'] = get_user_from_jwt(kwargs['jwt'])

        return msg, {'extra': extra}


class JSONFormatter(jsonlogger.JsonFormatter):
    """
    Format the LogRecord as a JSON.
    We use datadog for logging, and the datadog agent can't decode the
    default python pickled LogRecord. It can't decode a packed json either.
    """
    service = None

    def __init__(self, *args, **kwargs):
        self.service = kwargs.pop('service', 'unknown service')

        super().__init__(*args, **kwargs)

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)

        log_record['service'] = self.service


class JSONDatagramHandler(DatagramHandler):
    """
    DatagramHandler using JSONFormatter
    """

    def __init__(self, host, port, service=None):
        super().__init__(host, port)

        supported_keys = [
            'asctime',
            'created',
            'filename',
            'funcName',
            'levelname',
            'levelno',
            'lineno',
            'module',
            'msecs',
            'message',
            'name',
            'pathname',
            'process',
            'processName',
            'relativeCreated',
            'thread',
            'threadName'
        ]
        custom_format = ' '.join('%({0:s})'.format(k) for k in supported_keys)
        self.formatter = JSONFormatter(custom_format, service=service)

    def makePickle(self, record):
        return self.formatter.format(record).encode() + b'\n'
