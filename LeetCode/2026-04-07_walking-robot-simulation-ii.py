from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perim = 2 * (width + height) - 4
        self.pos = 0
        self.started = False

    def step(self, num: int) -> None:
        if self.perim == 0:
            return
        
        self.started = True
        self.pos = (self.pos + num) % self.perim

    def getPos(self) -> List[int]:
        p = self.pos
        
        if p < self.w:
            return [p, 0]
        p -= self.w
        
        if p < self.h - 1:
            return [self.w - 1, p + 1]
        p -= (self.h - 1)
        
        if p < self.w - 1:
            return [self.w - 2 - p, self.h - 1]
        p -= (self.w - 1)
        
        return [0, self.h - 2 - p]

    def getDir(self) -> str:
        if self.pos == 0:
            return "East" if not self.started else "South"
        
        p = self.pos
        
        if p < self.w:
            return "East"
        p -= self.w
        
        if p < self.h - 1:
            return "North"
        p -= (self.h - 1)
        
        if p < self.w - 1:
            return "West"
        
        return "South"