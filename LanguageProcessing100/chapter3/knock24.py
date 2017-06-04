import re

if __name__ == "__main__":

    with open("british_articles.txt") as file:
        lines = file.readlines()
    
    file_pattern = re.compile("(File|ファイル):(.*?)\|")

    for line in lines:
        file_line = re.search(file_pattern, line)
        if file_line is not None:
            print(file_line.group(2))
