from sqlalchemy import or_

from flask import current_app
from models.companies import Companies
from utils.common import tag_converter


class SearchInternalService(object):
    def __init__(self, company_tag: str):
        self._company_tag = company_tag

    def __repr__(self):
        return f"self._company_tag : {self._company_tag}"

    def get_companies_by_tag(self):
        """
        get company list which include self._company_tag
        :return:
        """
        try:
            companies = []

            result, tags = tag_converter(tag=self._company_tag)

            if not result:
                raise ValueError(tags)

            rows = Companies.query.filter(Companies.tag_ko.like(f"%{tags['ko']}%")).all()

            rows = [row for row in rows if tags["ko"] in row.tag_ko.split("|")]

            for row in rows:
                if row.company_ko:
                    companies.append({"company_name": row.company_ko})
                elif row.company_ja:
                    companies.append({"company_name": row.company_ja})
                else:
                    companies.append({"company_name": row.company_en})

            if not companies:
                return None, "EMPTY"

        except Exception as e:
            current_app.logger.error(e)
            return False, "BAD_REQUEST"

        return True, {"companies": companies, "total_count": len(companies)}

