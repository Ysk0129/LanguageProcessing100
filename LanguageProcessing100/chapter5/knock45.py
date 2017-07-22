import knock41
from sentence import Sentence

if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        sentence = Sentence(chunks)

        lines = {}
        for pair in sentence.make_dependency_pairs():
            src = pair[0]
            dst = pair[1]

            particles = src.get_morphs_by_pos("助詞")
            verbs = dst.get_morphs_by_pos("動詞")

            if len(particles) != 0 and len(verbs) != 0:
                #動詞は最左のみ(問題参照)
                if verbs[0].base not in lines.keys():
                    lines[verbs[0].base] = " ".join([particle.base for particle in particles])
                else:
                    lines[verbs[0].base] += " " + " ".join([particle.base for particle in particles])

        with open("corpus.txt", "a") as f:
            for k, v in lines.items():
                f.write(k + "\t" + v + "\n")
