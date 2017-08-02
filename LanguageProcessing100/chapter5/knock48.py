import knock41
from sentence import Sentence

if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        sentence = Sentence(chunks)
        dependency_paths = sentence.make_dependency_paths()
        lines = []
        for path in dependency_paths:
            if "名詞" not in path[0].get_included_pos():
                continue

            lines.append(" -> ".join([chunk.get_phrase() for chunk in path]))

        with open("corpus4.txt", "a") as f:
            for line in lines:
                f.write(line + "\n")
