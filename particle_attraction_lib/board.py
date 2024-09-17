from dataclasses import dataclass

@dataclass
class Board:
    width: int
    height: int

    def __iter__(self):
        for dimension in (self.width, self.height):
            yield dimension