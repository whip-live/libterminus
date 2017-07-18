import jwt

from marshmallow import fields, Schema, validates, ValidationError


class Typology(Schema):
    typology = fields.Field(required=True)

    @validates('typology')
    def validate_typology(self, value):
        typology = ['moto', 'bike']
        if value not in typology:
            raise ValidationError('Invalid Typology')


class JWT(Schema):
    jwt = fields.Field(required=True)

    @validates('jwt')
    def validate_jwt(self, value):
        try:
            jwt.decode(value, verify=False, algorithms=['HS256'])
        except jwt.exceptions.DecodeError:
            raise ValidationError('Invalid JWT')


class DeviceDataSchema(Typology, JWT):
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


class RecordingSchema(Typology, JWT):
    id = fields.UUID(required=True)
    started = fields.Integer(required=True)
    ended = fields.Integer(required=True)
    points = fields.Nested(PointSchema, many=True)


class SectorSchema(Schema):
    name = fields.String()
    id = fields.UUID()
    start_index = fields.Integer()
    end_index = fields.Integer()


class MatchRecordingSchema(JWT):
    id = fields.UUID(required=True)
    bbox = fields.List(fields.Decimal())
    path = fields.Dict()
    sectors = fields.Nested(SectorSchema, many=True)
    points = fields.List(fields.Dict())


class MatchIndexSchema(Schema):
    segment_id = fields.List(fields.Field())
