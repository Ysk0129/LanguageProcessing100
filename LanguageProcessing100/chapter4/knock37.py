import knock30, knock36
import matplotlib, numpy, re
matplotlib.use("Agg")
from matplotlib.font_manager import FontProperties
from matplotlib import pyplot

def plot_word_occurrences_graph(dic, limit, **graph_elements):

    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:limit]
    x = [item[0] for item in sorted_dic]
    y = [item[1] for item in sorted_dic]
    fig = pyplot.figure(figsize=(10, 10))
    font = FontProperties(fname="/usr/share/fonts/VLGothic/VL-Gothic-Regular.ttf", size=14)
    ax1 = fig.add_subplot(111)
    ax1.bar(numpy.arange(len(x)), y, align="center")
    ax1.set_xticks(numpy.arange(len(x)))
    ax1.set_xticklabels(x, fontproperties=font)
    
    if "xlabel" in graph_elements:
        ax1.set_xlabel(graph_elements["xlabel"])
    if "ylabel" in graph_elements:
        ax1.set_ylabel(graph_elements["ylabel"])
    if "title" in graph_elements:
        ax1.set_title(graph_elements["title"])
    if "file_name" in graph_elements:
        file_name = graph_elements["file_name"]
    else:
        file_name = "graph"
    fig.savefig(file_name + ".png")

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    exclusion_pattern = re.compile("^[ぁ-ん]{1,2}$")
    exclusion_func = lambda w: re.match(exclusion_pattern, w) is not None
    occurrences_dict = knock36.count_occurrences_words(morphemes, pos_list=["助詞", "助動詞", "記号"], condition=exclusion_func)

    plot_word_occurrences_graph(occurrences_dict, 10, xlabel="Words", ylabel="Occurrences", title="Top 10 occurrences words", file_name="top10_occurrences_words")
