import knock41, knock42
import pydotplus

def plot_digraph(chunks, file_name):
    edges = []
    for pair in knock42.make_dependency_pairs(chunks):
        src = pair[0]
        dst = pair[1]
        edges.append([src.get_phrase(), dst.get_phrase()])

    graph = pydotplus.graph_from_edges(edges)
    graph.write_jpeg(file_name, prog="dot")


if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")
    chunks = chunks_list[10]
    plot_digraph(chunks, "digraph.jpg")
