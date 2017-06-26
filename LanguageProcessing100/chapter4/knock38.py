import knock30, knock36
import matplotlib, numpy, re
matplotlib.use("Agg")
from matplotlib.font_manager import FontProperties
from matplotlib import pyplot

def plot_dcit_histogram(dic, max, **graph_elements):
    
    sorted_dic = sorted(dic.values(), reverse=True)

    fig = pyplot.figure(figsize=(10, 10))
    font = FontProperties(fname="/usr/share/fonts/VLGothic/VL-Gothic-Regular.ttf", size=14)
    ax = fig.add_subplot(111)
    ax.hist(sorted_dic, bins=max, range=(0, max))

    if "xlabel" in graph_elements:
        ax.set_xlabel(graph_elements["xlabel"])
    if "ylabel" in graph_elements:
        ax.set_ylabel(graph_elements["ylabel"])
    if "title" in graph_elements:
        ax.set_title(graph_elements["title"])
    if "file_name" in graph_elements:
        file_name = graph_elements["file_name"]
    else:
        file_name = "graph"

    fig.savefig(file_name + ".png")

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    exclusion_pattern = re.compile("^[ぁ-ん]$")
    exclusion_func = lambda w: re.match(exclusion_pattern, w) is not None
    occurrences_dict = knock36.count_occurrences_words(morphemes, pos_list=["助詞", "助動詞", "記号"], condition=exclusion_func)

    plot_dcit_histogram(occurrences_dict, 50, xlabel="Occurrences", ylabel="Words",title="Occurrences words histogram", file_name="histogram_occurrences_words")
