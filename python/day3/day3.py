from typing import List
from dataclasses import dataclass
from functools import reduce


def load_input_text() -> List[str]:
    with open("python/day3/day-3-input.txt") as f:
        input = f.readlines()
    return [i.strip() for i in input]


@dataclass
class Point:
    x: int
    y: int

@dataclass
class Move:
    x: int
    y: int

@dataclass
class LocalGeology:
    layout: List[str]
    position: Point
    movement: Move

    def move(self):
        self.position = Point(self.position.x + self.movement.x, self.position.y + self.movement.y)
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

    def slide_to_end():
        pass



if __name__=="__main__":
    movement_choices = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    movement_tree_sum = []

    for choice in movement_choices:
        start = Point(0,0)
        r = LocalGeology(load_input_text(), start, Move(*choice))
        sum = 0
        while not r.has_reached_end():
            r = r.move()
            sum += r.is_on_tree()
        movement_tree_sum.append(sum)
        
    
    print(reduce(lambda a,b: a*b, movement_tree_sum))