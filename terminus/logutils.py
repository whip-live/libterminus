import jwt
import json
import logging

from logging.handlers import DatagramHandler


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


class JSONFormatter(logging.Formatter):
    """
    Format the LogRecord as a JSON.
    We use datadog for logging, and the datadog agent can't decode the
    default python pickled LogRecord. It can't decode a packed json either.
    """

    service = None

    def __init__(self, fmt=None, datefmt=None, style='%', service=None):
        self.service = service
        super().__init__(fmt, datefmt, style)

    def format(self, record):
        """
        This formatter fills the JSON with all the properies of the LogRecord,
        extra fields included, except the ones in the `skip_list` array
        """
        log = {
            'asctime': self.formatTime(record, self.datefmt),
        }
        skip_list = ('args', 'exc_info', 'exc_text', 'stack_info', 'msg')
        for key, value in record.__dict__.items():
            if key in skip_list:
                continue
            log.update({key: value})

        if self.service:
            log.update({'service': self.service})
        # NOTE: The new line is needed otherwise the agent will not send the packet
        return ("%s\n" % json.dumps(log)).encode()


class JSONDatagramHandler(DatagramHandler):
    """
    DatagramHandler using JSONFormatter
    """

    def __init__(self, host, port, service=None):
        super().__init__(host, port)
        self.formatter = JSONFormatter(service=service)

    def makePickle(self, record):
        return self.formatter.format(record)
