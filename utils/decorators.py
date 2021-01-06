import json

from copy import deepcopy

from flask import Response, request


def formatting_response(func):
    """
    Make fixed API response format
    :param func: function
    :return:
    """
    def wrapper(*args, **kwargs):
        res, result, status = func(*args, **kwargs)

        if result:
            res_copy = deepcopy(res)
            res_copy['result'] = result
            res = res_copy
        resp = json.dumps(obj=res, ensure_ascii=False, default=str).encode(encoding="utf-8")
        return Response(response=resp, content_type="application/json; charset=utf-8", status=status)
    return wrapper