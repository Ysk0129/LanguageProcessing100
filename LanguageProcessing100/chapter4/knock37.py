import knock30, knock36
import matplotlib, numpy, re
matplotlib.use("Agg")
from matplotlib.font_manager import FontProperties
from matplotlib import pyplot

def plot_dcit_graph(dic, limit):
    
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:limit]
    x = [item[0] for item in sorted_dic]
    y = [item[1] for item in sorted_dic]
    fig = pyplot.figure(figsize=(10, 10))
    font = FontProperties(fname="/usr/share/fonts/VLGothic/VL-Gothic-Regular.ttf", size=14)
    ax1 = fig.add_subplot(111)
    ax1.bar(numpy.arange(len(x)), y, align="center")
    ax1.set_xticks(numpy.arange(len(x)))
    ax1.set_xticklabels(x, fontproperties=font)
    ax1.set_ylabel("Occurrences")
    ax1.set_title("Top 10 occurrences words")

    fig.savefig("top10_occurrences_words.png")

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    exclusion_pattern = re.compile("^[ぁ-ん]$")
    exclusion_func = lambda w: re.match(exclusion_pattern, w) is not None
    occurrences_dict = knock36.count_occurrences_words(morphemes, pos_list=["助詞", "助動詞", "記号"], condition=exclusion_func)

    plot_dcit_graph(occurrences_dict, 10)
