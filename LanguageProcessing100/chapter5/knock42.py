import knock41
from sentence import Sentence

if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        sentence = Sentence(chunks)
        for pair in sentence.make_dependency_pairs():
            print(pair[0].get_phrase() + "\t" + pair[1].get_phrase())
