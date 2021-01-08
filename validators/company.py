from marshmallow import Schema, fields
from marshmallow.validate import Length, Regexp


class CompanyPostSchema(Schema):
    company_tag_regex = "^[tag,태그,タグ]+_[0-9]+$"
    company_name = fields.Str(required=True, allow_none=False, validate=Length(min=1))
    company_tag = fields.Str(required=True, allow_none=False, validate=Regexp(company_tag_regex))


class CompanyDeleteSchema(Schema):
    company_tag_regex = "^[tag,태그,タグ]+_[0-9]+$"
    company_name = fields.Str(required=True, allow_none=False, validate=Length(min=1))
    company_tag = fields.Str(required=True, allow_none=False, validate=Regexp(company_tag_regex))