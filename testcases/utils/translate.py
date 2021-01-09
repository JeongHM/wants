# import unittest
#
# from utils.translate import Translator
#
#
# class TranslateTest(unittest.TestCase):
#     def setUp(self) -> None:
#         self._korean = "태그"
#         self._japan = "タグ"
#         self._english = "tag"
#
#     def test_get_language_country_method_korean(self):
#         translate = Translator(text=self._korean)
#         country = translate.get_language_country()
#         self.assertEqual("ko", country)
#
#     def test_get_language_country_method_japan(self):
#         translate = Translator(text=self._japan)
#         country = translate.get_language_country()
#         self.assertEqual("ja", country)
#
#     def test_get_language_country_method_english(self):
#         translate = Translator(text=self._english)
#         country = translate.get_language_country()
#         self.assertEqual("en", country)
#
#     def test_get_text_other_county_method_korean_to_english(self):
#         translate = Translator(text=self._korean)
#         text = translate.get_text_other_county(country="en")
#         self.assertEqual(self._english, text)
#
#     def test_get_text_other_county_method_korean_to_japan(self):
#         translate = Translator(text=self._korean)
#         text = translate.get_text_other_county(country="ja")
#         self.assertEqual(self._japan, text)
#
#     def test_get_text_all_country_method(self):
#         texts = [self._korean, self._japan]
#
#         result = sorted([text.split("_")[0] for text in texts])
#         for text in texts:
#             translate = Translator(text=text.split("_")[0])
#             method_result = sorted([text for country, text in translate.get_text_all_country().items()])
#             self.assertEqual(result, method_result)
#
#
# if __name__ == '__main__':
#     unittest.main()
