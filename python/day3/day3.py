from typing import List
from dataclasses import dataclass

def load_input_text() -> List[str]:
    with open("python/day3/day-3-input.txt") as f:
        input = f.readlines()
    return [i.strip() for i in input]


@dataclass
class Point:
    x: int
    y: int

@dataclass
class LocalGeology:
    layout: List[str]
    position: Point

    def move(self, x: int, y: int):
        self.position = Point(self.position.x + x, self.position.y + y)
        
        self.position.x = self.position.x % len(self.layout[0])

        return self
    
    def is_on_tree(self):
        if self.layout[self.position.y][self.position.x] == "#":
            return True
        else:
            return False

    def has_reached_end(self):
        if self.position.y >= len(self.layout) - 1:
            return True
        else:
            return False



if __name__=="__main__":
    start = Point(0,0)
    r = LocalGeology(load_input_text(), start)
    sum = 0
    while not r.has_reached_end():
        r = r.move(3,1)
        sum += r.is_on_tree()
    print(sum)