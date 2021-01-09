from flask import Blueprint, request

from utils.decorators import formatting_response
from utils.response_codes import RESPONSE_CODE

from services.internals.auto_complete import AutoCompleteInternalService

auto_complete_blueprint = Blueprint(name="auto_complete", import_name=__name__)


@auto_complete_blueprint.route(rule="", methods=["GET"], endpoint="auto_complete")
@formatting_response
def auto_complete():

    company_name = request.args.get("company_name") if request.args else None

    search_service = AutoCompleteInternalService(company_name=company_name)

    result, message = search_service.get_companies_by_name()
    if result is None:
        return RESPONSE_CODE[message], {}, 204
    if result is False:
        return RESPONSE_CODE[message], {}, 400

    return RESPONSE_CODE["SUCCESS"], message, 200