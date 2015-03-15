from itertools import chain

phi = 1.61803398875

class PenroseModel:
    def __init__(self, start_state):
        self.tiles = start_state
        self.history = []

    def split(self):
        self.history.append(list(self.tiles))
        self.tiles = list(chain(*[tile.split() for tile in self.tiles]))

    def desplit(self):
        if self.history:
            self.tiles = self.history.pop()

    def get_tiles(self):
        return self.tiles

class HalfDart:
    def __init__(self, A,B,C):
        self.a = A
        self.b = B
        self.c = C

    def split(self):
        a,b,c = self.a,self.b,self.c
        ax, ay = self.a
        cx, cy = self.c

        fx = cx + (ax-cx)*(1/phi)
        fy = cy + (ay-cy)*(1/phi)
        f = (fx,fy)
        return [HalfKite(f, c, b),HalfDart(b, f, a)]

class HalfKite:
    def __init__(self, A,B,C):
        self.a = A
        self.b = B
        self.c = C

    def split(self):
        a,b,c = self.a,self.b,self.c
        ax, ay = self.a
        bx, by = self.b
        cx, cy = self.c

        gx = bx + (cx-bx)*(1/phi)
        gy = by + (cy-by)*(1/phi)
        g = (gx,gy)

        fx = bx + (ax-bx)*(1/(phi**2))
        fy = by + (ay-by)*(1/(phi**2))
        f = (fx,fy)

        return [HalfDart(g,f,b),
                HalfKite(c,a,g),
                HalfKite(f,a,g),]
