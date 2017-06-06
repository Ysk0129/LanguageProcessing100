import knock25
import re

if __name__ == "__main__":
    with open("british_articles.txt") as file:
        text = file.read()

    basic_info = knock25.extract_basic_info(text)
    field_pairs = knock25.extract_field_dict(basic_info)

    strong_pattern = re.compile(r"'{2,5}")

    for k, v in field_pairs.items():
        trimmed_k = re.sub(strong_pattern, "", k)
        trimmed_v = re.sub(strong_pattern, "", v)
        print(trimmed_k + " = " + trimmed_v)
