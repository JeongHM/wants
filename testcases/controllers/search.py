import json
import unittest
import requests

from utils.response_codes import RESPONSE_CODE


class SearchControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        set up host, parameter
        :return: None
        """
        self._host = "http://localhost:5000/search"

    def test_get_search_method_success(self):
        params = [
            {
                "company_tag": "태그_19"
            },
            {
                "company_tag": "tag_19"
            },
            {
                "company_tag": "タグ_19"
            }
        ]

        for param in params:
            req = requests.get(url=self._host,
                               params=param,
                               headers={"Context-Type": "application/json"})

            resp = req.json()
            del resp["result"]
            self.assertEqual(resp, RESPONSE_CODE["SUCCESS"])

    def test_get_search_method_empty(self):
        params = [
            {
                "company_tag": "태그_20000"
            },
            {
                "company_tag": "tag_20000"
            },
            {
                "company_tag": "タグ_20000"
            }
        ]
        for param in params:
            req = requests.get(url=self._host,
                               params=param,
                               headers={"Context-Type": "application/json"})

            status = req.status_code
            self.assertEqual(204, status)


if __name__ == '__main__':
    unittest.main()