import jwt
import logging
import uuid


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

    def process(self, msg, kwargs):
        extra = kwargs.get("extra", {})
        if "recording" in kwargs:
            # We expect recording to be an instance of recording_pb2.Recording
            recording = kwargs["recording"]
            # The UUIDs are serialized as array of bytes instead of strings
            # because they occupy half the size.
            # See `messages/terminus/proto/recording.proto`
            extra["device_id"] = recording.device_id
            extra["recording_id"] = str(uuid.UUID(bytes=recording.id))
            # Add to extra metadata the JWT payload
            extra["user"] = get_user_from_jwt(recording.jwt)

        elif "topic" in kwargs:
            extra["topic"] = kwargs["topic"]
        elif "device_id" in kwargs:
            extra["device_id"] = kwargs["device_id"]
        elif "recording_id" in kwargs:
            extra["recording_id"] = kwargs["recording_id"]
        elif "jwt" in kwargs:
            extra["user"] = get_user_from_jwt(kwargs["jwt"])

        return msg, {"extra": extra}
