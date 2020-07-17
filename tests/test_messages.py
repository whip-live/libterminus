import uuid

from datetime import datetime, timezone, timedelta

from terminus.proto import device_data_pb2
from terminus.proto import areas_to_match_pb2
from terminus.proto import recording_pb2
from terminus.proto import recordings_matches_pb2
from terminus.proto import recordings_to_match_pb2
from terminus.proto import core_pb2


def test_areas_to_match(recording_message):
    areas_to_match = areas_to_match_pb2.AreasToMatch()
    areas_to_match.recordings.append(recording_message)
    area = areas_to_match_pb2.AreasToMatch.Area()
    area.id = uuid.uuid4().bytes
    area.polygon.lats.append(43.0000001)
    area.polygon.lons.append(43.0000001)
    areas_to_match.areas.append(area)
    assert areas_to_match.ByteSize() == 741


def test_recordings_matches(recording_message):
    recordings_matches = recordings_matches_pb2.RecordingsMatches()
    # Add recording first
    recordings_matches.recording.CopyFrom(recording_message)

    # Create matching_id
    segment_id = uuid.uuid4()
    recording_id = uuid.uuid4()

    matching_id = recordings_matches_pb2.RecordingsMatches.MatchingId()
    matching_id.segment_id = segment_id.bytes

    matching = recordings_matches_pb2.RecordingsMatches.MatchingId.Matching()
    matching.matching_id = recording_id.bytes
    matching.start_index = 0
    matching.end_index = 1

    # Add matching to matching_id.matchings
    matching_id.matchings.append(matching)

    # Create matching segment struct
    index = recordings_matches_pb2.RecordingsMatches.MatchingSegment.Index()
    index.start = 0
    index.end = 10
    recordings_matches.matching_segments[segment_id.hex].indexes.append(index)

    recordings_matches.matching_ids.append(matching_id)
    assert recordings_matches.ByteSize() == 783


def test_recordings_to_match_message(recording_message):
    # Create RecordingsToMatch instance
    recordings_to_match = recordings_to_match_pb2.RecordingsToMatch()
    # Add recording from fixture
    recordings_to_match.recordings.append(recording_message)
    # Create a segment
    segment = recordings_to_match_pb2.RecordingsToMatch.Segment()
    segment.id = uuid.uuid4().bytes
    segment.path.lats.append(42.0020202)
    segment.path.lons.append(42.0020202)
    segment.start_line.lats.append(42.0020202)
    segment.start_line.lons.append(42.0020202)
    segment.end_line.lats.append(42.0020202)
    segment.end_line.lons.append(42.0020202)

    # Add the segment
    recordings_to_match.segments.append(segment)
    # Test serialization works
    recordings_to_match.SerializeToString()
    # Assert size
    assert recordings_to_match.ByteSize() == 785


def test_recording_proto_message():
    # Calculate timestamp in milliseconds
    now = datetime(2020, 1, 1, tzinfo=timezone.utc)
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    # Start an hour ago, end now
    started = (now - epoch - timedelta(hours=1)) // timedelta(milliseconds=1)
    ended = (now - epoch) // timedelta(milliseconds=1)

    recording = recording_pb2.Recording()
    recording.jwt = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6I"
        "kpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
        ".SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )
    recording.typology = core_pb2.Typology.MOTO
    recording.id = uuid.uuid4().bytes
    recording.user_id = uuid.uuid4().bytes
    recording.activity_id = uuid.uuid4().bytes
    recording.device_id = str(uuid.uuid4())
    recording.started = started
    recording.ended = ended
    # Add some points
    for i in range(10):
        point = recording_pb2.Recording.Point()
        point.time = int(started + (ended - started) / 10 * i)
        point.speed = i * 0.1
        point.position_lat = i * 0.0000001
        point.position_lon = i * 0.0000001
        point.ele = i * 0.1
        point.pdop = i
        point.hdop = i * 0.1
        recording.points.append(point)

        ccu2_data_point = recording.ccu2_data_points.add()
        ccu2_data_point.gear = 1
        ccu2_data_point.rpm = 1000
        ccu2_data_point.throttle = 120
        ccu2_data_point.mapswitchmode = 2

    # Test serialization works
    recording.SerializeToString()
    assert recording.ByteSize() == 806


def test_device_data_proto_message():
    device_data = device_data_pb2.DeviceData()
    device_data.content = uuid.uuid4().bytes
    device_data.jwt = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6I"
        "kpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
        ".SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )
    device_data.user_id = uuid.uuid4().bytes
    device_data.activity_id = uuid.uuid4().bytes
    device_data.device_id = str(uuid.uuid4())
    device_data.recording_id = uuid.uuid4().bytes
    device_data.typology = core_pb2.Typology.MOTO
    device_data.content_format = device_data_pb2.DeviceDataFormat.KTM_CSV_1
    device_data.SerializeToString()
    assert device_data.ByteSize() == 270
