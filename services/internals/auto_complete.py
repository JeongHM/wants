from sqlalchemy import or_

from flask import current_app
from models.companies import Companies


class AutoCompleteInternalService(object):
    def __init__(self, company_name: str):
        self._company_name = company_name

    def __repr__(self):
        return f"self._company_name : {self._company_name}"

    def get_companies_by_name(self):
        """
        get company list which include self._company_name
        :return:
        """
        try:
            companies = []
            rows = Companies.query.filter(or_(Companies.company_ko.like(f"{self._company_name}%"),
                                              Companies.company_ja.like(f"{self._company_name}%"),
                                              Companies.company_en.like(f"{self._company_name}%"))).all()

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
