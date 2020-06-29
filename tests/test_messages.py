import uuid

from datetime import datetime, timezone, timedelta

from terminus.proto import device_data_pb2
from terminus.proto import recording_pb2
from terminus.proto import core_pb2


def test_recording_proto_message():

    # Calculate timestamp in milliseconds
    now = datetime.now(timezone.utc)
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
    recording.device_id = uuid.uuid4().bytes
    recording.started = started
    recording.ended = ended
    # Add some points
    for i in range(10):
        point = recording_pb2.Recording.Point()
        point.sequence_id = i
        point.time = started + (ended - started) / 10 * i
        point.speed = i * 0.1
        point.position_lat = i * 0.0000001
        point.position_lon = i * 0.0000001
        point.ele = i * 0.1
        point.pdop = i
        point.hdop = i * 0.1
        recording.points.append(point)
    assert recording.ByteSize() == 642


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
    device_data.device_id = uuid.uuid4().bytes
    device_data.recording_id = uuid.uuid4().bytes
    device_data.typology = core_pb2.Typology.MOTO
    device_data.content_format = device_data_pb2.DeviceDataFormat.KTM_CSV_1
    device_data.SerializeToString()
    assert device_data.ByteSize() == 250
