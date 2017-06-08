from knock25 import extract_basic_info, extract_field_dict
from knock26 import trim_strong
import re

def trim_internal_link(text):
    internal_link_pattern = re.compile(r"(.*?)\[\[(.*?)\]\](.*?)")
    matched_texts = re.search(internal_link_pattern, text)

    if matched_texts is not None and not ":" in matched_texts.group(2):
        return matched_texts.group(1) + matched_texts.group(2) + matched_texts.group(3)
    else:
        return text

if __name__ == "__main__":
    with open("british_articles.txt") as file:
        text = file.read()

    basic_info = extract_basic_info(text)
    field_pairs = extract_field_dict(basic_info)

    for k, v in field_pairs.items():
        trimmed_k = trim_internal_link(trim_strong(k))
        trimmed_v = trim_internal_link(trim_strong(v))
        print(trimmed_k + " = " + trimmed_v)
