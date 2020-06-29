import jwt
import logging

from logging.handlers import DatagramHandler

from pythonjsonlogger import jsonlogger


def get_user_from_jwt(token):
    """
    Decode the JWT to read the payload
    """
    decoded_payload = jwt.decode(token, verify=False, algorithms=["HS256"])
    if "username" in decoded_payload:
        return decoded_payload["username"]
    else:
        return decoded_payload["user_id"]


class RecordingAdapter(logging.LoggerAdapter):
    """
    This adapter adds extra fields to a LogRecord
    """

    metadata = {}

    @classmethod
    def set_metadata(cls, **kwargs):
        cls.metadata = {}

        if "jwt" in kwargs:
            jwt = kwargs.pop("jwt")
            cls.metadata["user"] = get_user_from_jwt(jwt)

        cls.metadata.update(kwargs)

    @classmethod
    def clear_metadata(cls):
        cls.metadata = {}

    def process(self, msg, kwargs):
        extra = kwargs.get("extra", {})
        extra.update(**self.metadata)
        return msg, {"extra": extra}


class JSONFormatter(jsonlogger.JsonFormatter):
    """
    Format the LogRecord as a JSON.
    We use datadog for logging, and the datadog agent can't decode the
    default python pickled LogRecord. It can't decode a packed json either.
    """

    service = None

    def __init__(self, *args, **kwargs):
        self.service = kwargs.pop("service", "unknown service")

        super().__init__(*args, **kwargs)

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)

        log_record["service"] = self.service


class JSONDatagramHandler(DatagramHandler):
    """
    DatagramHandler using JSONFormatter
    """

    def __init__(self, host, port, service=None):
        super().__init__(host, port)

        supported_keys = [
            "asctime",
            "created",
            "filename",
            "funcName",
            "levelname",
            "levelno",
            "lineno",
            "module",
            "msecs",
            "message",
            "name",
            "pathname",
            "process",
            "processName",
            "relativeCreated",
            "thread",
            "threadName",
        ]
        custom_format = " ".join("%({0:s})".format(k) for k in supported_keys)
        self.formatter = JSONFormatter(custom_format, service=service)

    def makePickle(self, record):
        return self.formatter.format(record).encode() + b"\n"
