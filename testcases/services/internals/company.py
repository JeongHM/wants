import unittest

from utils.common import tag_converter


class CompanyInternalServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._valid_bodies = [
            {
                "company_name": "원티드랩",
                "company_tag": "태그_1"
            },
            {
                "company_name": "OKAY.com",
                "company_tag": "タグ_4"
            },
            {
                "company_name": "株式会社ZMP",
                "company_tag": "tag_28"
            },
        ]

        self._invalid_body = {
            "company_name": "TE스트",
            "company_tag": "TE그_일"
        }

    def test_tag_converter_method_with_valid_param(self):
        _tags = {
            "원티드랩": ["태그_1", "タグ_1", "tag_1"],
            "OKAY.com": ["태그_4", "タグ_4", "tag_4"],
            "株式会社ZMP": ["태그_28", "タグ_28", "tag_28"]
        }
        for valid_body in self._valid_bodies:
            company_tag = valid_body.get("company_tag")
            result, tags = tag_converter(tag=company_tag)

            self.assertEqual(True, result)
            self.assertEqual(sorted(_tags.get(valid_body.get("company_name"))), sorted(tags.values()))


if __name__ == '__main__':
    unittest.main()