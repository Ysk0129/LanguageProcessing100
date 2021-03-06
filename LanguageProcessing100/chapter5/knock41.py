import knock40
from chunk import Chunk, CHUNK_LINE_PATTERN
from morph import Morph
import re

def make_chunk_list(lattice_format_sentence):

    chunks = []

    srcs = 0
    dst = 0
    morphs = []
    for line in lattice_format_sentence:
        
        ch_mached = CHUNK_LINE_PATTERN.match(line)
        if ch_mached is not None:
            if len(morphs) != 0: chunks.append(Chunk(srcs, dst, morphs))
            srcs = ch_mached.group(1)
            dst = ch_mached.group(2)
            morphs = []
            continue
        
        elements = line.replace("\t", ",").split(",")
        if len(elements) >= 8:
            base = elements[7] if elements[7] != "*" else elements[0]
            morph = Morph(elements[0], elements[7], elements[1], elements[2])
            morphs.append(morph)
    if len(morphs) != 0: chunks.append(Chunk(srcs, dst, morphs))

    return chunks

def make_chunks_list(lattice_format_filename):
    chunks_list = []
    sentences = knock40.group_by_sentence(lattice_format_filename)
    for sentence in sentences:
        chunks_list.append(make_chunk_list(sentence))
    return chunks_list

if __name__ == "__main__":

    chunks_list = make_chunks_list("neko.txt.cabocha")

    print([str(chunk) for chunk in chunks_list[8]])
