import re

class Chunk:

    def __init__(self, srcs, dst, morphs):
        self.srcs = srcs
        self.dst = dst
        self.morphs = morphs
    
    def __str__(self):
        return "srcs: {0}, dst: {1}, morphs: {2}".format(self.srcs, self.dst, [str(morph) for morph in self.morphs])


CHUNK_LINE_PATTERN = re.compile(r"^\*\s(\d+)\s(-?\d+)D\s(\d+/\d+)+\s(-|\d|\.)+\n$")
