from flask import Blueprint, request
from services.internals.company import CompanyInternalService

from utils.decorators import formatting_response
from utils.response_codes import RESPONSE_CODE

company_blueprint = Blueprint(name="company", import_name=__name__)


@company_blueprint.route(rule="/tags", methods=["POST", "DELETE"], endpoint="company_tags")
@formatting_response
def company_tags():

    # POST method Logic
    if request.method == "POST":
        body = request.get_json()
        company_service = CompanyInternalService(body=body)

        validate, message = company_service.validate_body()

        # validate request body
        if not validate:
            return RESPONSE_CODE["VALIDATE_FAIL"], message, 400 # Bad Request

        result, message = company_service.create_company_tags()

        if result is None:
            if message == "EMPTY":
                return RESPONSE_CODE[message], {}, 204 # EMPTY
            return RESPONSE_CODE[message], {}, 409 # ALREADY_EXIST

        return RESPONSE_CODE[message], None, 200

    # DELETE method Logic
    params = dict(request.args) if request.args else None

    company_service = CompanyInternalService(param=params)

    validate, message = company_service.validate_param()

    if not validate:
        return RESPONSE_CODE["VALIDATE_FAIL"], message, 400  # Bad Request

    result, message = company_service.delete_company_tags()

    if result is None:
        return RESPONSE_CODE[message], {}, 204  # EMPTY

    return RESPONSE_CODE[message], None, 200
