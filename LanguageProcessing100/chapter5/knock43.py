import knock41, knock42

if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        for pair in knock42.make_dependency_pairs(chunks):
            src = pair[0]
            dst = pair[1]
            if "名詞" in src.get_included_pos() and "動詞" in dst.get_included_pos():
                print(src.get_phrase() + "\t" + dst.get_phrase())
