import datetime

from terminus.schema import BaseSchema, DeviceDataSchema, RecordingSchema


def test_base_schema(encoded_jwt):
    """
    Test the base schema
    """
    data = {
        'jwt': encoded_jwt,
        'typology': 'moto'
    }
    result = BaseSchema().load(data)
    assert result.errors == {}


def test_device_data_schema(encoded_jwt):
    """
    Test the device_data schema
    """
    data = {
        'jwt': encoded_jwt,
        'typology': 'bike',
        'device_id': '8dc51b75-03d1-4140-9768-10a3586882e9',
        'recording_id': 'fd3fe49e-2c5a-4c24-a317-18c057c8c036',
        'user_id': '6fb46cfd-bb6e-4ff3-9b16-bbfbd2a45164',
        'activity_id': '82051d4a-1616-4016-9560-cd2a1755a8ea',
    }
    result = DeviceDataSchema().load(data)
    assert result.errors == {}


def test_schema_with_valid_data(encoded_jwt):
    """
    Test recording schema with invalid JWT
    """
    data = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'started': 232323,
        'ended': 23232,
        'typology': 'moto',
        'jwt': encoded_jwt,
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


def test_schema_with_invalid_typology(encoded_jwt):
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
        'jwt': encoded_jwt,
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
