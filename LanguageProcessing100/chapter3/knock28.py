import knock25
import re

def trim_all_markup(text):
    markup_pattern = re.compile(r"'{2,5}|\[|\]|<.*?>|(File|ファイル):|(Category|カテゴリ):|\||#REDIRECT|~~~~|<!--\s.*?\s-->|=|{|}|\*")
    return re.sub(markup_pattern, "", text)

if __name__ == "__main__":
    with open("british_articles.txt") as file:
        text = file.read()
    
    basic_info = knock25.extract_basic_info(text)
    print(trim_all_markup(basic_info))
