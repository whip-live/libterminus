import datetime

from terminus.schema import RecordingSchema


def test_schema_with_valid_data():
    """
    Test recording schema with invalid JWT
    """
    data = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'device_id': '5decc93d-ea32-41c4-9bf8-82e1d74c772f',
        'activity_id': '0b119ed7-7333-46a0-ada1-c469a610ddd0',
        'user_id': 'efbbb33c-f143-4f2d-a2f4-9d5d41df7d85',
        'recording_id': 'd856a420-a04f-4328-b22e-d8f7bb12904a',
        'started': 232323,
        'ended': 23232,
        'typology': 'moto',
        'jwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmb28iOiJiYXIiLCJuYW1lIjoiYWxkbyJ9.ZkBDRTfnQhJ6jxU2JtO7a0mAvL7S7smufpivvMO4mt8', # noqa
        'points': [
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 1), (0, 2)],
                'geoidheight': 323,
                'fix': '3d',
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            },
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 3), (0, 4)],
                'geoidheight': 323,
                'fix': '3d',
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            }]
    }
    result = RecordingSchema().load(data)
    assert result.errors == {}


def test_schema_with_invalid_jwt():
    """
    Test recording schema
    """
    data = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'device_id': '5decc93d-ea32-41c4-9bf8-82e1d74c772f',
        'activity_id': '0b119ed7-7333-46a0-ada1-c469a610ddd0',
        'user_id': 'efbbb33c-f143-4f2d-a2f4-9d5d41df7d85',
        'recording_id': 'd856a420-a04f-4328-b22e-d8f7bb12904a',
        'started': 232323,
        'ended': 23232,
        'typology': 'moto',
        'jwt': 'aaa.bbb.ccc',
        'points': [
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 1), (0, 2)],
                'geoidheight': 323,
                'fix': '3d',
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            },
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 3), (0, 4)],
                'geoidheight': 323,
                'fix': '3d',
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            }]
    }
    result = RecordingSchema().load(data)
    assert result.errors == {'jwt': ['Invalid JWT']}


def test_schema_with_invalid_typology():
    """
    Test recording schema with invalid typology
    """
    data = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'device_id': '5decc93d-ea32-41c4-9bf8-82e1d74c772f',
        'activity_id': '0b119ed7-7333-46a0-ada1-c469a610ddd0',
        'user_id': 'efbbb33c-f143-4f2d-a2f4-9d5d41df7d85',
        'recording_id': 'd856a420-a04f-4328-b22e-d8f7bb12904a',
        'started': 232323,
        'ended': 23232,
        'typology': 'foo',
        'jwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmb28iOiJiYXIiLCJuYW1lIjoiYWxkbyJ9.ZkBDRTfnQhJ6jxU2JtO7a0mAvL7S7smufpivvMO4mt8', # noqa
        'points': [
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 1), (0, 2)],
                'geoidheight': 323,
                'fix': '3d',
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            },
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 3), (0, 4)],
                'geoidheight': 323,
                'fix': '3d',
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            }]
    }
    result = RecordingSchema().load(data)
    assert result.errors == {'typology': ['Invalid Typology']}
