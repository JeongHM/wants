def tag_converter(tag: str) -> (bool, dict):
    """
    tag name convert all language tag name -> tag_converter(text=tag_name)
    :param tag: tag_name (태그, タグ, tag)
    :return: list
    """
    try:
        tags = {
            "ko": "태그",
            "ja": "タグ",
            "en": "tag"
        }
        tag_name, tag_number = tag.split("_")

        if tag_name not in tags.values():
            raise ValueError("Text not in tags.values()")

        result = {country: name + "_" + tag_number for country, name in tags.items()}

    except Exception as e:
        return False, e

    return True, result