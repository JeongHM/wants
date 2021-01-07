# from google_trans_new import google_translator
#
#
# class Translator(object):
#     def __init__(self, text: str):
#         self._text = text
#         self._translator = google_translator()
#
#     def __repr__(self):
#         return f"self._text : {self._text}"
#
#     def get_language_country(self) -> str:
#         """
#         get self._text language country
#         :param text: text
#         :return: [ko, korea]
#         """
#         return self._translator.detect(text=self._text)[0]
#
#     def get_text_other_county(self, country) -> str:
#         """
#         translate text to country language > self._text = korea, country = ko -> 한국
#         :param text: text
#         :param country: ja, en, ko
#         :return:
#         """
#         return self._translator.translate(text=self._text, lang_tgt=country).strip()
#
#     def get_text_all_country(self) -> dict:
#         """
#         get japan, english, korean text by self._text
#         :return: [태그_1, tag_1, タグ_1]
#         """
#         translate_countries = {"ja", "en", "ko"}
#
#         result = {c: self.get_text_other_county(country=c).strip() for c in translate_countries}
#         return result
