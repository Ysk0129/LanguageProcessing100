import MeCab

def output_analyzed_file(file_name):
    with open(file_name) as file:
        text = file.read()
    with open("{}.mecab".format(file_name), "w") as file:
        tagger = MeCab.Tagger("-Ochasen")
        file.write(tagger.parse(text))

if __name__ == "__main__":
    output_analyzed_file("neko.txt")
