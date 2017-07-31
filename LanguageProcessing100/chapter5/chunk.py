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

    def get_morphs_by_pos(self, pos):
        return [morph for morph in self.morphs if pos in morph.pos]

    def get_morphs(self, func):
        return func(self.morphs)

    def get_included_pos(self):
        return [morph.pos for morph in self.morphs]
    
    def get_included_pos1(self):
        return [morph.pos1 for morph in self.morphs]

    def get_included_surfaces(self):
        return [morph.surface for morph in self.morphs]

    def replace_surface(self, pos, new_surface):
        for i in range(0, len(self.morphs)):
            if self.morphs[i].pos == pos:
                self.morphs[i].surface = new_surface

CHUNK_LINE_PATTERN = re.compile(r"^\*\s(\d+)\s(-?\d+)D\s(\d+/\d+)+\s(-|\d|\.)+\n$")
