import re

class Chunk:

    def __init__(self, srcs, dst, morphs):
        self.srcs = srcs
        self.dst = dst
        self.morphs = morphs
    
    def __str__(self):
        return "srcs: {0}, dst: {1}, morphs: {2}".format(self.srcs, self.dst, [str(morph) for morph in self.morphs])

    def remove_marks(self):
        self.morphs = [morph for morph in self.morphs if not morph.is_mark()]

    def get_phrase(self):
        return "".join(morph.surface for morph in self.morphs)

    def get_included_pos(self):
        return [morph.pos for morph in self.morphs]

CHUNK_LINE_PATTERN = re.compile(r"^\*\s(\d+)\s(-?\d+)D\s(\d+/\d+)+\s(-|\d|\.)+\n$")
