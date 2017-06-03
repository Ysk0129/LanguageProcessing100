import re

if __name__ == "__main__":

    with open("british_articles.txt") as file:
        lines = file.readlines()
    
    section_pattern = re.compile("^(=+)\s*(.*?)\s*(=+)$")
    for line in lines:
        section = re.search(section_pattern, line)
        if section is not None:
            section_name = section.group(2)
            section_level = str(len(section.group(1)) - 1)
            print(section_name + " : " + section_level)
