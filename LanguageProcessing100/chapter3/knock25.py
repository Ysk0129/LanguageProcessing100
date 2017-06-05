import re

def extract_basic_info(text):
    basic_info_pattern = re.compile(r"^\{\{基礎情報.*?\n(^|.*?)^\}\}", re.MULTILINE + re.DOTALL)
    basic_info = re.search(basic_info_pattern, text).group(1)
    return basic_info

def extract_field_dict(text):
    field_pattern = re.compile(r"^\|(.*?)\s\=\s(.*?)(?=\n\|)", re.MULTILINE + re.DOTALL)
    field_dict = dict(field_pattern.findall(text))
    return field_dict

if __name__ == "__main__":
    with open("british_articles.txt") as file:
        text = file.read()

    basic_info = extract_basic_info(text)
    field_pairs = extract_field_dict(basic_info)

    for k, v in field_pairs.items():
        print(k + " = " + v)
