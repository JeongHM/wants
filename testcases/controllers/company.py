import json
import unittest
import requests

from utils.response_codes import RESPONSE_CODE


class CompanyControllerTest(unittest.TestCase):
    """
    Test /company controller TestCase
    """
    def setUp(self) -> None:
        """
        set up host, parameter
        :return: None
        """
        self._host = "http://localhost:5000/company"
        self._tags_path = "/tags"

    def test_post_company_tags_method_success(self):
        """
        test [POST] /company/tags success
        :return:
        """
        params = {
            "company_name": "원티드랩",
            "company_tag": "태그_112"
        }
        req = requests.post(url=self._host + self._tags_path,
                            data=json.dumps(params),
                            headers={'Content-Type': 'application/json'})

        resp = req.json()
        self.assertEqual(resp, RESPONSE_CODE["SUCCESS"])

    def test_post_company_tags_method_empty(self):
        """
        test [POST] /company/tags when company_name is not in database
        :return:
        """
        params = {
            "company_name": "이런회사는없습니다",
            "company_tag": "태그_12"
        }
        req = requests.post(url=self._host + self._tags_path,
                            data=json.dumps(params),
                            headers={'Content-Type': 'application/json'})

        status_code = req.status_code
        self.assertEqual(status_code, 204)

    def test_post_company_tags_method_conflict(self):
        """
        test [POST] /company/tags when company_tags is already exists
        :return:
        """
        params = {
            "company_name": "원티드랩",
            "company_tag": "태그_4"
        }
        req = requests.post(url=self._host + self._tags_path,
                            data=json.dumps(params),
                            headers={'Content-Type': 'application/json'})

        resp = req.json()
        self.assertEqual(resp, RESPONSE_CODE["ALREADY_EXIST"])

    def test_delete_company_tags_method_success(self):
        """
        test [DELETE] /company/tags success
        :return:
        """
        params = {
            "company_name": "원티드랩",
            "company_tag": "태그_4"
        }
        req = requests.delete(url=self._host + self._tags_path,
                              params=params,
                              headers={'Content-Type': 'application/json'})
        resp = req.json()
        self.assertEqual(resp, RESPONSE_CODE["SUCCESS"])

    def test_delete_company_tags_method_empty(self):
        pass

    def test_delete_company_tags_method_validation_fail(self):
        pass


if __name__ == '__main__':
    unittest.main()