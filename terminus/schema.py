import jwt

from marshmallow import fields, Schema, validate, ValidationError


def validate_jwt(value):
    try:
        jwt.decode(value, verify=False, algorithms=['HS256'])
    except jwt.exceptions.DecodeError:
        raise ValidationError('Invalid JWT')


class DeviceDataSchema(Schema):
    jwt = fields.Field(required=True, validate=validate_jwt)
    typology = fields.String(required=True, validate=validate.OneOf(['moto', 'bike']))
    device_id = fields.UUID(required=True)
    recording_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    activity_id = fields.UUID(required=True)


class PointSchema(Schema):
    sequence_id = fields.Integer()
    ele = fields.Float()
    time = fields.DateTime()
    course = fields.Float()
    speed = fields.Float()
    position = fields.Field()
    geoidheight = fields.Float()
    fix = fields.Integer(validate=validate.Range(min=0, max=8))
    sat = fields.Integer()
    hdop = fields.Float()
    vdop = fields.Float()
    pdop = fields.Float()


class PathSchema(Schema):
    coordinates = fields.List(fields.List(fields.Decimal), required=True)


class RecordingSchema(Schema):
    """
    Data structure expected in `recordings` (mallow, sutt) and
    `path_proposal` (sutt, bliss, isaac)
    """
    jwt = fields.Field(required=True, validate=validate_jwt)
    typology = fields.String(required=True, validate=validate.OneOf(['moto', 'bike']))
    id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    activity_id = fields.UUID(required=True)
    device_id = fields.UUID(required=True)
    started = fields.DateTime(required=True)
    ended = fields.DateTime(required=True)
    points = fields.Nested(PointSchema, many=True)
    path = fields.Nested(PathSchema)


class MatchRecordingSchema(Schema):
    """
    recording part of the expected message in `recordings_matches`.

    `recording_matches` is a tuple composed by 3 elements: recording,
    matching_segments, matching_ids. This is the first part
    """
    id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    activity_id = fields.UUID(required=True)
    jwt = fields.Field(required=True, validate=validate_jwt)
    bbox = fields.List(fields.Decimal())
    path = fields.Nested(PathSchema)
    points = fields.List(fields.Dict())


class SectorSchema(Schema):
    name = fields.String()
    id = fields.UUID()
    start_index = fields.Integer()
    end_index = fields.Integer()


class MatchSchema(Schema):
    indexes = fields.List(fields.Field(), required=True)
    bbox = fields.List(fields.Integer(), required=True)
    path = fields.Nested(PathSchema, required=True)
    sectors = fields.Nested(SectorSchema, many=True)


class MatchingSegmentSchema(Schema):
    """
    matched_segment part of the expected message in `recordings_matches`

    `recording_matches` is a tuple composed by 3 elements: recording,
    matching_segments, matching_ids. This is the second part
    """
    segment_id = fields.Nested(MatchSchema)


class MatchIndexSchema(Schema):
    """
    matching_ids part of the expected message in `recording_matches`

    `recording_matches` is a tuple composed by 3 elements: recording,
    matching_segments, matching_ids. This is the third part
    """
    segment_id = fields.List(fields.Field())
