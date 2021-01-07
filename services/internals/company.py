from sqlalchemy import or_
from flask import current_app

from models import db
from models.companies import Companies
from validators.company import CompanyPostSchema, CompanyDeleteSchema


class CompanyInternalService(object):
    """
    Company Internal Service Logic Class
    -> CompanyInternalService(compnay_name, tags)
    """
    def __init__(self, param: dict = None, body: dict = None):
        self._param = param
        self._body = body

    def __repr__(self):
        return f"self._param : {self._param} self._body : {self._body}"

    def tag_converter(self, tag: str) -> (bool, dict):
        """
        tag name convert all language tag name -> tag_converter(text=tag_name)
        :param tag: tag_name (태그, タグ, tag)
        :return: list
        """
        try:
            tags = {
                "ko": "태그",
                "ja": "タグ",
                "en": "tag"
            }
            tag_name, tag_number = tag.split("_")

            if tag_name not in tags.values():
                raise ValueError("Text not in tags.values()")

            result = {country: name + "_" + tag_number for country, name in tags.items()}

        except Exception as e:
            return False, e

        return True, result

    def validate_body(self) -> (bool, bool):
        """
        Validate [POST, DELETE] /company/tags body value
        :return: boolean
        """
        try:
            error = CompanyPostSchema().validate(data=self._body)
            if error:
                raise ValueError(error)

        except ValueError as e:
            current_app.logger.error(e)
            return False, e

        return True, True

    def has_company_tags(self, company_name: str, company_tag: str) -> (bool or None, bool):
        """
        check company has request tag name in database
        :return: boolean (True, False)
        """

        try:
            row = Companies.query.filter(or_(Companies.company_ko == company_name,
                                             Companies.company_en == company_name,
                                             Companies.company_ja == company_name)).first()
            if not row:
                return None, None

            # Set ko, ja, en tags
            tags = row.tag_ko.split("|") + row.tag_en.split("|") + row.tag_ja.split("|")

            # Already Exist tag
            if company_tag in tags:
                return True, True

        except Exception as e:
            current_app.logger.error(e)

        return False, True

    def create_company_tags(self) -> (bool or None, str):
        """
        create company tags
        :return: bool or None
        """
        session = db.session()

        try:
            company_name = self._body.get("company_name")
            company_tag = self._body.get("company_tag")

            result, code = self.has_company_tags(company_name=company_name, company_tag=company_tag)

            # There is no request body company name in database
            if result is None:
                return None, "EMPTY"

            # Already company has request body company tag
            if result is True and code is True:
                return None, "ALREADY_EXIST"

            result, tags = self.tag_converter(tag=company_tag)

            if not result:
                raise ValueError(tags)

            # select row
            row = session.query(Companies).filter((Companies.company_ko == company_name) |
                                                  (Companies.company_en == company_name) |
                                                  (Companies.company_ja == company_name)).first()

            tag_ko = "|".join(row.tag_ko.split("|") + [tags["ko"]]) if row.tag_ko else tags["ko"]
            tag_ja = "|".join(row.tag_ja.split("|") + [tags["ja"]]) if row.tag_ja else tags["ja"]
            tag_en = "|".join(row.tag_en.split("|") + [tags["en"]]) if row.tag_en else tags["en"]

            # update row
            session.query(Companies).filter((Companies.company_ko == company_name) |
                                            (Companies.company_en == company_name) |
                                            (Companies.company_ja == company_name))\
                .update({
                    "tag_ko": tag_ko,
                    "tag_ja": tag_ja,
                    "tag_en": tag_en
            })

        except Exception as e:
            current_app.logger.error(e)
            session.rollback()
            return False, "BAD_REQUEST"

        session.commit()
        return True, "SUCCESS"

    def delete_company_tags(self) -> (bool or None, str):
        """
        delete company tags
        :return: bool, String
        """

        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            return False, "BAD_REQUEST"

        return True, "SUCCESS"