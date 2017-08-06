import knock41
from sentence import Sentence

if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        sentence = Sentence(chunks)
        dependency_paths = sentence.make_dependency_paths()
        lines = []
        lines2 = []
        
        first = ""
        last = ""
        for path in dependency_paths:
            if "名詞" not in path[0].get_included_pos():
                continue
            
            if first == "" and last == "":
                path[0].replace_surface("名詞", "X")
                first = path[0].get_phrase() + " | "
                last = " | " + path[-1].get_phrase()
                continue

            path[0].replace_surface("名詞", "Y")

            lines.append(first + " -> ".join([chunk.get_phrase() for chunk in path[0:-1]]) + last)

            if len(path) >= 2:
                path[0].replace_surface("名詞", "X")
                for i in reversed(range(1, len(path) - 1)):
                    if "名詞" in path[i].get_included_pos():
                        phrase = " -> ".join([chunk.get_phrase() for chunk in path[0:i]])
                        lines2.append(phrase + " -> Y")
        
        first = ""
        last = ""
        with open("corpus5.txt", "a") as f:
            for line in lines:
                f.write(line + "\n")

            for line in lines2:
                f.write(line + "\n")
