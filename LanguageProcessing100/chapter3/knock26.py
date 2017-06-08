import knock25
import re

def trim_strong(text):
    strong_pattern = re.compile(r"'{2,5}")
    trimmed = re.sub(strong_pattern, "", text)
    return trimmed

if __name__ == "__main__":
    with open("british_articles.txt") as file:
        text = file.read()

    basic_info = knock25.extract_basic_info(text)
    field_pairs = knock25.extract_field_dict(basic_info)

    for k, v in field_pairs.items():
        trimmed_k = trim_strong(k)
        trimmed_v = trim_strong(v)
        print(trimmed_k + " = " + trimmed_v)
