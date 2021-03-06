import chunk

class Sentence:

    def __init__(self, chunks):
        self.chunks = chunks
    
    def __str__(self):
        str_sentence = ""
        for chunk in self.chunks:
            str_sentence += chunk.get_phrase()
        return str_sentence

    def make_dependency_pairs(self):

        dependency_pairs = []
        for chunk in self.chunks:
            if chunk.dst == "-1":
                continue

            chunk.remove_marks()
            dst_chunk = self.chunks[int(chunk.dst)]
            dst_chunk.remove_marks()
            if len(chunk.morphs) != 0 and len(dst_chunk.morphs) != 0:
                pair = (chunk, dst_chunk)
                dependency_pairs.append(pair)

        return dependency_pairs

    def make_dependency_paths(self):

        dependency_paths = []
        for chunk in self.chunks:
            if chunk.dst == "-1":
                continue
                
            chunk.remove_marks()

            dependency_path = [chunk]
            dst = chunk.dst
            while(dst != "-1"):
                dst_chunk = self.chunks[int(dst)]
                dst_chunk.remove_marks()
                dependency_path.append(dst_chunk)
                dst = dst_chunk.dst

            dependency_paths.append(dependency_path)
            
        return dependency_paths
