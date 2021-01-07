from marshmallow import Schema, fields
from marshmallow.validate import Length


class CompanyPostSchema(Schema):
    company_name = fields.Str(required=True, allow_none=False, validate=Length(min=1))
    company_tag = fields.Str(required=True, allow_none=False, validate=Length(min=1))
