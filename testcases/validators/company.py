import unittest

from validators.company import CompanyPostSchema, CompanyDeleteSchema


class CompanyValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self._valid_objects = [
            {
                "company_name": "원티드랩",
                "company_tag": "태그_1"
            },
            {
                "company_name": "infobank",
                "company_tag": "tag_25"
            },
            {
                "company_name": "株式会社SM Entertainment Japan",
                "company_tag": "タグ_28"
            }
        ]
        self._invalid_objects = [
            {
                "company_name": "원티드랩",
                "company_tag": "태그_@"
            },
            {
                "company_name": "infobank",
                "company_tag": "tag_t"
            },
            {
                "company_name": "株式会社SM Entertainment Japan",
                "company_tag": "タグ_태그"
            }
        ]

    def test_post_schema_with_valid(self):
        """
        Test CompanyPostSchema valid object
        :return:
        """

        for obj in self._valid_objects:
            self.assertEqual({}, CompanyPostSchema().validate(data=obj))

    def test_post_schema_with_invalid(self):
        """
        Test CompanyPostSchema invalid object
        :return:
        """
        error_message = {'company_tag': ['String does not match expected pattern.']}

        for obj in self._invalid_objects:
            message = CompanyPostSchema().validate(data=obj)
            self.assertEqual(error_message, message)


    def test_delete_schema_with_valid(self):
        """
        Test CompanyDeleteSchema valid object
        :return:
        """
        for obj in self._valid_objects:
            self.assertEqual({}, CompanyDeleteSchema().validate(data=obj))

    def test_delete_schema_with_invalid(self):
        """
        Test CompanyDeleteSchema invalid object
        :return:
        """
        error_message = {'company_tag': ['String does not match expected pattern.']}

        for obj in self._invalid_objects:
            message = CompanyDeleteSchema().validate(data=obj)
            self.assertEqual(error_message, message)


if __name__ == '__main__':
    unittest.main()