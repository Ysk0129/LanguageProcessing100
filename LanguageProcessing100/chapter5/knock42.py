import knock41

def make_dependency_pairs(chunks):

    dependency_pairs = []
    for chunk in chunks:
        if chunk.dst == "-1":
            continue

        chunk.remove_marks()
        dst_chunk = chunks[int(chunk.dst)]
        dst_chunk.remove_marks()
        if len(chunk.morphs) != 0 and len(dst_chunk.morphs) != 0:
            pair = (chunk, dst_chunk)
            dependency_pairs.append(pair)

    return dependency_pairs
    
if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        for pair in make_dependency_pairs(chunks):
            print(pair[0].get_phrase() + "\t" + pair[1].get_phrase())
