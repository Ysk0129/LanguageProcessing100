import re

if __name__ == "__main__":

    with open("british_articles.txt") as file:
        lines = file.readlines()

    category_pattern = re.compile("^\[\[Category:(.*)\]\]")
    for line in lines:
        category = re.search(category_pattern, line)
        if category is not None:
            print(category.group(1))
