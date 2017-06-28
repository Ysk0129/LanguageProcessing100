import knock30, knock36
import matplotlib, numpy, re
matplotlib.use("Agg")
from matplotlib.font_manager import FontProperties
from matplotlib import pyplot

def plot_dcit_histogram(dic, max, **graph_elements):
    
    sorted_occurrences = sorted(dic.values(), reverse=True)
    rank = list(range(1, len(sorted_occurrences) + 1))

    fig = pyplot.figure(figsize=(10, 10))
    font = FontProperties(fname="/usr/share/fonts/VLGothic/VL-Gothic-Regular.ttf", size=14)
    ax = fig.add_subplot(111)
    ax.plot(sorted_occurrences, rank)

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
    
    ax.set_xscale("log")
    ax.set_yscale("log")
    fig.savefig(file_name + ".png")

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    exclusion_pattern = re.compile("^[ぁ-ん]$")
    exclusion_func = lambda w: re.match(exclusion_pattern, w) is not None
    occurrences_dict = knock36.count_occurrences_words(morphemes, pos_list=["助詞", "助動詞", "記号"], condition=exclusion_func)

    plot_dcit_histogram(occurrences_dict, 50, xlabel="Rank", ylabel="Occurrences",title="Occurrences words histogram", file_name="both_log_word_occurrence")
