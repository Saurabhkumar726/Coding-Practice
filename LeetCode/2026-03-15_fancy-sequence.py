class Fancy:

    def __init__(self):
        self.mod = 10**9 + 7
        self.seq = []
        self.mul = 1
        self.add = 0

    def modinv(self, x):
        return pow(x, self.mod - 2, self.mod)

    def append(self, val: int) -> None:
        v = (val - self.add) % self.mod
        v = (v * self.modinv(self.mul)) % self.mod
        self.seq.append(v)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod