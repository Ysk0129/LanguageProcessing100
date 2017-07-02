
class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface: {0}, base: {1}, pos: {2}, po1: {3}".format(self.surface, self.base, self.pos, self.pos1)
