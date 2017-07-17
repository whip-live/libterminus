import jwt

from marshmallow import fields, Schema, validates, ValidationError


class BaseSchema(Schema):
    typology = fields.Field(required=True)
    jwt = fields.Field(required=True)

    @validates('typology')
    def validate_typology(self, value):
        typology = ['moto', 'bike']
        if value not in typology:
            raise ValidationError('Invalid Typology')

    @validates('jwt')
    def validate_jwt(self, value):
        try:
            jwt.decode(value, verify=False, algorithms=['HS256'])
        except jwt.exceptions.DecodeError:
            raise ValidationError('Invalid JWT')


class DeviceDataSchema(BaseSchema):
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


class RecordingSchema(BaseSchema):
    id = fields.UUID(required=True)
    started = fields.Integer(required=True)
    ended = fields.Integer(required=True)
    points = fields.Nested(PointSchema, many=True)
