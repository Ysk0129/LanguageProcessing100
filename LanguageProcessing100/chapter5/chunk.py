class Chunk:

    def __init__(morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    
    def __str__(self):
        return "morphs: {0}, dst: {1}, srcs: {2}".format([str(morph) for morph in self.morphs], self.dst, self.srcs)
