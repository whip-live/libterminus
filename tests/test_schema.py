import datetime

from terminus.schema import (
    DeviceDataSchema,
    RecordingSchema,
    MatchRecordingSchema,
    MatchIndexSchema,
)


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
        'started': datetime.datetime.now().isoformat(),
        'ended': datetime.datetime.now().isoformat(),
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
        'started': datetime.datetime.now().isoformat(),
        'ended': datetime.datetime.now().isoformat(),
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
        'started': datetime.datetime.now().isoformat(),
        'ended': datetime.datetime.now().isoformat(),
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
    assert result.errors == {'typology': ['Not a valid choice.']}


def test_match_recording_schema():
    """
    Test the MatchRecordingSchema
    """
    data = {
        'id': '653a4136-e378-4790-809a-01cffe30e3ed',
        'bbox': (0, 0, 1, 1),
        'path': {
            'coordinates': [
                [0.00001, 0.00001],
                [0.00002, 0.00002],
                [0.00003, 0.00003]
            ]
        },
        'sectors': [
            {'id': '4fe8c832-13be-43b1-b358-3558d32f4b82', 'name': 'Sector 1', 'start_index': 1, 'end_index': 2},
            {'id': 'baa9ec35-c982-4934-a72b-fc3565313802', 'name': 'Sector 2', 'start_index': 2, 'end_index': 3},
            {'id': '98f211b7-3fd6-4843-8b0a-75033373e38c', 'name': 'Sector 3', 'start_index': 3, 'end_index': 4}
        ]
    }
    result = MatchRecordingSchema(exclude=('jwt', )).load(data)
    assert result.errors == {}


def test_match_recording_schema_without_some_fields(encoded_jwt):
    """
    Test the MatchRecordingSchema
    """
    data = {
        'jwt': encoded_jwt,
        'id': '653a4136-e378-4790-809a-01cffe30e3ed',
        'bbox': (0, 0, 1, 1),
        'path': {
            'coordinates': [
                [0.00001, 0.00001],
                [0.00002, 0.00002],
                [0.00003, 0.00003]
            ]
        },
        'points': [
            {'position': 'POINT(0.0002 0.0002)'},
            {'position': 'POINT(0.0003 0.0003)'},
            {'position': 'POINT(0.0004 0.0004)'},
        ]
    }
    result = MatchRecordingSchema(exclude=('sectors', )).load(data)
    assert result.errors == {}


def test_match_segment_schema():
    data = {'segment_id': [(0, 2)]}
    result = MatchIndexSchema().load(data)
    assert result.errors == {}
