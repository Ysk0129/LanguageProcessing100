import json

if __name__ == "__main__":

    output_texts = []

    with open("jawiki-country.json") as file:
        line = file.readline()

        while line:
            wiki_json = json.loads(line)
            if wiki_json["title"] == "イギリス":
                output_texts.append(wiki_json["text"])
            line = file.readline()

    with open("british_articles.txt", "w") as file:
        file.writelines(output_texts)
    