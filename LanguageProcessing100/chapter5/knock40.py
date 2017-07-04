from morph import Morph
import re
from chunk import CHUNK_LINE_PATTERN

def group_by_sentence(lattice_format_filename):

    sentenes = []

    with open(lattice_format_filename) as file:
        line = file.readline()

        eos = "EOS\n"
        sentence = []
        
        while line:
            if line == eos:
                if len(sentence) != 0:
                    sentenes.append(sentence)
                    sentence = []
                line = file.readline()
                continue
            sentence.append(line)
            line = file.readline()

    return sentenes

def remove_chunk_lines(lattice_format_lines):

    removed = [line for line in lattice_format_lines if CHUNK_LINE_PATTERN.match(line) is None]

    return removed

def make_morph_list(lattice_format_lines):

    morph_list = []

    for line in remove_chunk_lines(lattice_format_lines):
        elements = line.replace("\t", ",").split(",")
        if len(elements) == 10:
            morph = Morph(elements[0], elements[7], elements[1], elements[2])
            morph_list.append(morph)

    return morph_list

if __name__ == "__main__":

    sentences = group_by_sentence("neko.txt.cabocha")
    morph_sentences = []

    for sentence in sentences:
        morph_list = make_morph_list(sentence)
        morph_sentences.append(morph_list)
    
    for morph in morph_sentences[2]:
        print(morph)
