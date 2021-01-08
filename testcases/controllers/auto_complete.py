import unittest
import requests

from utils.response_codes import RESPONSE_CODE


class AutoCompleteControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self._host = "http://localhost:5000/auto-complete"
        self._valid_company_names = [
            {
                "company_name": "원티"
            },
            {
                "company_name": "株"
            },
            {
                "company_name": "wa"
            }
        ]

        self._invalid_ko_company_name = "꿹뾝뙦"

    def test_get_auto_complete_with_valid(self):
        for param in self._valid_company_names:
            req = requests.get(url=self._host,
                               params=param,
                               headers={"Content-Type": "application/json"})

            resp = req.json()
            del resp["result"]
            self.assertEqual(RESPONSE_CODE["SUCCESS"], resp)

    def test_get_auto_complete_with_invalid(self):
        req = requests.get(url=self._host,
                           params=self._invalid_ko_company_name,
                           headers={"Content-Type": "application/json"})

        status_code = req.status_code
        self.assertEqual(204, status_code)


if __name__ == '__main__':
    unittest.main()