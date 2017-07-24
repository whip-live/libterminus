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


class RecordingSchema(Schema):
    jwt = fields.Field(required=True, validate=validate_jwt)
    typology = fields.String(required=True, validate=validate.OneOf(['moto', 'bike']))
    id = fields.UUID(required=True)
    started = fields.DateTime(required=True)
    ended = fields.DateTime(required=True)
    points = fields.Nested(PointSchema, many=True)


class SectorSchema(Schema):
    name = fields.String()
    id = fields.UUID()
    start_index = fields.Integer()
    end_index = fields.Integer()


class MatchRecordingSchema(Schema):
    id = fields.UUID(required=True)
    jwt = fields.Field(required=True, validate=validate_jwt)
    bbox = fields.List(fields.Decimal())
    path = fields.Dict()
    points = fields.List(fields.Dict())


class MatchSchema(Schema):
    indexes = fields.List(fields.Field(), required=True)
    bbox = fields.List(fields.Integer(), required=True)
    path = fields.Dict(required=True)
    sectors = fields.Nested(SectorSchema, many=True)


class MatchingSegmentSchema(Schema):
    segment_id = fields.Nested(MatchSchema)


class MatchIndexSchema(Schema):
    segment_id = fields.List(fields.Field())
