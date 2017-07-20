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
    fix = fields.String()
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
    sectors = fields.Nested(SectorSchema, many=True)
    points = fields.List(fields.Dict())


class MatchIndexSchema(Schema):
    segment_id = fields.List(fields.Field())
