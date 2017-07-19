import knock41
from sentence import Sentence
import pydotplus

def plot_digraph(sentence, file_name):
    edges = []
    for pair in sentence.make_dependency_pairs():
        src = pair[0]
        dst = pair[1]
        edges.append([src.get_phrase(), dst.get_phrase()])

    graph = pydotplus.graph_from_edges(edges)
    graph.write_jpeg(file_name, prog="dot")


if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")
    sentence = Sentence(chunks_list[10])
    plot_digraph(sentence, "digraph.jpg")
