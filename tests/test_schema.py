import datetime
import uuid

from terminus.schema import (
    AreaSchema,
    AreasToMatch,
    DeviceDataSchema,
    RecordingSchema,
    PathProposalSchema,
    MatchRecordingSchema,
    MatchingSegmentSchema,
    MatchIndexSchema,
    SegmentSchema,
    RecordingsToMatchSchema
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
        'content_format': 'livex-1',
    }
    result = DeviceDataSchema().load(data)
    assert result.errors == {}


def test_schema_with_valid_data(encoded_jwt):
    """
    Test recording schema
    """
    data = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'user_id': '57a1cffe-6652-4804-b655-e9ea40fe65e6',
        'activity_id': '8fd923ef-fc12-4a8a-9bae-3fe5329135c8',
        'device_id': 'cd80ac71-5fe8-472e-90b1-23c2a4491c98',
        'started': datetime.datetime.now().isoformat(),
        'ended': datetime.datetime.now().isoformat(),
        'typology': 'moto',
        'jwt': encoded_jwt,
        'path': {
            'coordinates': [
                [0.00001, 0.00001],
                [0.00002, 0.00002]
            ]
        },
        'points': [
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 1), (0, 2)],
                'geoidheight': 323,
                'fix': 1,
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            },
            {
                'sequence_id': 2,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 3), (0, 4)],
                'geoidheight': 323,
                'fix': 1,
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            }]
    }
    result = RecordingSchema().load(data)
    assert result.errors == {}


def test_schema_with_invalid_jwt():
    """
    Test recording schema with invalid JWT
    """
    data = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'user_id': '57a1cffe-6652-4804-b655-e9ea40fe65e6',
        'activity_id': '8fd923ef-fc12-4a8a-9bae-3fe5329135c8',
        'device_id': 'cd80ac71-5fe8-472e-90b1-23c2a4491c98',
        'started': datetime.datetime.now().isoformat(),
        'ended': datetime.datetime.now().isoformat(),
        'typology': 'moto',
        'jwt': 'aaa.bbb.ccc',
        'path': {
            'coordinates': [
                [0.00001, 0.00001],
                [0.00002, 0.00002]
            ]
        },
        'points': [
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 1), (0, 2)],
                'geoidheight': 323,
                'fix': 1,
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            },
            {
                'sequence_id': 2,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 3), (0, 4)],
                'geoidheight': 323,
                'fix': 1,
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
        'path': {
            'coordinates': [
                [0.00001, 0.00001],
                [0.00002, 0.00002]
            ]
        },
        'points': [
            {
                'sequence_id': 1,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 1), (0, 2)],
                'geoidheight': 323,
                'fix': 1,
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            },
            {
                'sequence_id': 2,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 3), (0, 4)],
                'geoidheight': 323,
                'fix': 1,
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            }]
    }
    result = RecordingSchema().load(data)
    assert result.errors == {'typology': ['Not a valid choice.']}


def test_schema_without_path(encoded_jwt):
    """
    Test path proposal schema without path
    """
    data = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'device_id': '5decc93d-ea32-41c4-9bf8-82e1d74c772f',
        'activity_id': '0b119ed7-7333-46a0-ada1-c469a610ddd0',
        'user_id': 'efbbb33c-f143-4f2d-a2f4-9d5d41df7d85',
        'recording_id': 'd856a420-a04f-4328-b22e-d8f7bb12904a',
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
                'fix': 1,
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            },
            {
                'sequence_id': 2,
                'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30,
                'speed': 90,
                'position': [(0, 3), (0, 4)],
                'geoidheight': 323,
                'fix': 1,
                'sat': 5,
                'hdop': 8,
                'pdop': 7,
            }]
    }
    result = PathProposalSchema().load(data)
    assert result.errors == {'path': {'coordinates': ['Missing data for required field.']}}


def test_match_segment_schema():
    """
    Test the MatchSegmentSchema
    """
    data = {
        'segment_id': {
            'indexes': [(0, 2)],
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
    }
    result = MatchingSegmentSchema().load(data)
    assert result.errors == {}


def test_match_recording_schema(encoded_jwt):
    """
    Test the MatchRecordingSchema
    """
    data = {
        'jwt': encoded_jwt,
        'id': '653a4136-e378-4790-809a-01cffe30e3ed',
        'user_id': '57a1cffe-6652-4804-b655-e9ea40fe65e6',
        'activity_id': '8fd923ef-fc12-4a8a-9bae-3fe5329135c8',
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
    result = MatchRecordingSchema().load(data)
    assert result.errors == {}


def test_match_recording_schema_failed(encoded_jwt):
    """
    Test the MatchRecordingSchema without the user_id
    """
    data = {
        'jwt': encoded_jwt,
        'id': '653a4136-e378-4790-809a-01cffe30e3ed',
        'activity_id': '8fd923ef-fc12-4a8a-9bae-3fe5329135c8',
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
    result = MatchRecordingSchema().load(data)
    assert result.errors == {'user_id': ['Missing data for required field.']}


def test_match_index_schema():
    data = [
        {
            'segment_id': '653a4136-e378-4790-809a-01cffe30e3ed',
            'matchings': [
                {
                    'matching_id': '8fd923ef-fc12-4a8a-9bae-3fe5329135c8',
                    'start_index': 3,
                    'end_index': 12,
                }
            ]
        }
    ]
    result = MatchIndexSchema(many=True).load(data)
    assert result.errors == {}


def test_segment_schema():
    """
    Test segment schema work sas expected
    """
    data = {
        'id': uuid.uuid4(),
        'name': 'fake name',
        'path': {'coordinates': [[0, 0], [1, 1]]},
        'public': True,
        'track_type': 'sand',
        'user': uuid.uuid4(),
        'sectors': [],
    }
    result = SegmentSchema().load(data)
    assert result.errors == {}


def test_recordings_to_match_schema_fails_if_no_data():
    """
    Test RecordingsToMatchSchema fails if no recordings or segments
    """
    data = {
        'recordings': [],
        'segments': []
    }
    result = RecordingsToMatchSchema().load(data)
    assert result.errors == {
        'recordings': ['At least one recording needed'],
        'segments': ['At least one segment needed']
    }


def test_recordings_to_match_schema_works(encoded_jwt):
    """
    Test RecordingsToMatchSchema works with correct data
    """
    recording = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'user_id': '57a1cffe-6652-4804-b655-e9ea40fe65e6',
        'activity_id': '8fd923ef-fc12-4a8a-9bae-3fe5329135c8',
        'device_id': 'cd80ac71-5fe8-472e-90b1-23c2a4491c98',
        'started': datetime.datetime.now().isoformat(),
        'ended': datetime.datetime.now().isoformat(),
        'typology': 'moto',
        'jwt': encoded_jwt,
        'path': {'coordinates': [[1, 1], [2, 2]]},
        'points': [
            {
                'sequence_id': 1, 'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30, 'speed': 90,
                'position': [(0, 1), (0, 2)], 'geoidheight': 323,
                'fix': 1, 'sat': 5, 'hdop': 8, 'pdop': 7,
            },
            {
                'sequence_id': 2, 'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30, 'speed': 90, 'position': [(0, 3), (0, 4)],
                'geoidheight': 323, 'fix': 1, 'sat': 5, 'hdop': 8, 'pdop': 7,
            }
        ]
    }

    segment = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'user': '57a1cffe-6652-4804-b655-e9ea40fe65e6',
        'name': 'fake',
        'path': {'coordinates': [[1, 1], [2, 2]]},
        'public': True,
        'track_type': 'sand',
        'sectors': [],
    }

    data = {
        'recordings': [recording],
        'segments': [segment]
    }
    result = RecordingsToMatchSchema().load(data)
    assert result.errors == {}


def test_area_schema():
    """
    Test Area Schema
    """
    area = {
        'id': 'b81930ee-86a7-4737-9c8e-eab65820ea0d',
        'user_id': '2eede4f3-10f6-4899-93f8-343b4b0a9ade',
        'title': 'Test Area',
        'private': False,
        'polygon': {
            'coordinates': [[[0.0, 0.0], [0.0, 50.0], [50.0, 50.0], [50.0, 0.0], [0.0, 0.0]]]
        },
        'tags': ['foo', 'bar', 'foobar']
    }
    result = AreaSchema().load(area)
    assert result.errors == {}


def test_area_schema_fails_missing_mandatory_fields():
    """
    Test empty Area Schema
    """
    result = AreaSchema().load({})
    assert result.errors == {
        'id': ['Missing data for required field.'],
        'title': ['Missing data for required field.'],
        'private': ['Missing data for required field.'],
        'polygon': ['Missing data for required field.'],
        'user_id': ['Missing data for required field.']
    }


def test_areas_to_match_schema_fail_empty_data(encoded_jwt):
    """
    Test that AreaToMatch Schema fails with empty data
    """
    data = {
        'areas': [],
        'recordings': []
    }
    result = AreasToMatch().load(data)
    assert result.errors == {
        'areas': ['At least one area needed'],
        'recordings': ['At least one recording needed']
    }


def test_areas_to_match_schema(encoded_jwt):
    """
    Test AreasToMatchSchema
    """
    area = {
        'id': 'b81930ee-86a7-4737-9c8e-eab65820ea0d',
        'user_id': '2eede4f3-10f6-4899-93f8-343b4b0a9ade',
        'title': 'Test Area',
        'private': False,
        'polygon': {
            'coordinates': [[[0.0, 0.0], [0.0, 50.0], [50.0, 50.0], [50.0, 0.0], [0.0, 0.0]]]
        },
        'tags': ['foo', 'bar', 'foobar']
    }

    recording = {
        'id': '01a61386-53ae-43bd-8586-d09acf88b391',
        'user_id': '57a1cffe-6652-4804-b655-e9ea40fe65e6',
        'activity_id': '8fd923ef-fc12-4a8a-9bae-3fe5329135c8',
        'device_id': 'cd80ac71-5fe8-472e-90b1-23c2a4491c98',
        'started': datetime.datetime.now().isoformat(),
        'ended': datetime.datetime.now().isoformat(),
        'typology': 'moto',
        'jwt': encoded_jwt,
        'path': {'coordinates': [[1, 1], [2, 2]]},
        'points': [
            {
                'sequence_id': 1, 'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30, 'speed': 90,
                'position': [(0, 1), (0, 2)], 'geoidheight': 323,
                'fix': 1, 'sat': 5, 'hdop': 8, 'pdop': 7,
            },
            {
                'sequence_id': 2, 'ele': 12,
                'time': datetime.datetime.now().isoformat(),
                'course': 30, 'speed': 90, 'position': [(0, 3), (0, 4)],
                'geoidheight': 323, 'fix': 1, 'sat': 5, 'hdop': 8, 'pdop': 7,
            }
        ]
    }

    data = {
        'areas': [area],
        'recordings': [recording]
    }
    result = AreasToMatch().load(data)
    assert result.errors == {}
