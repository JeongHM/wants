from flask import Blueprint, request

from utils.decorators import formatting_response
from utils.response_codes import RESPONSE_CODE
from services.internals.search import SearchInternalService

search_blueprint = Blueprint(name="search", import_name=__name__)


@search_blueprint.route(rule="", methods=["GET"], endpoint="search")
@formatting_response
def search():
    company_tag = request.args.get("company_tag") if request.args else None

    search_service = SearchInternalService(company_tag=company_tag)

    result, message = search_service.get_companies_by_tag()

    if result is None:
        return RESPONSE_CODE[message], {}, 204
    if result is False:
        return RESPONSE_CODE[message], {}, 400

    return RESPONSE_CODE["SUCCESS"], message, 200
