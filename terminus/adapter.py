import jwt

from logging import LoggerAdapter


def get_user_from_jwt(token):
    """
    Decode the JWT to read the payload
    """
    decoded_payload = jwt.decode(token, verify=False, algorithms=['HS256'])
    if 'username' in decoded_payload:
        return decoded_payload['username']
    else:
        return ''


class RecordingAdapter(LoggerAdapter):
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
