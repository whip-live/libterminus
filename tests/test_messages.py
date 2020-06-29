import uuid


def test_device_data_proto_message():
    from terminus.proto import device_data_pb2
    from terminus.proto import core_pb2

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
