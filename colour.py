from enum import Enum


class Colour(Enum):
    WHITE = "#fff"
    GREY = "#808080"
    GREEN = "#55A41C"
    RED = "#C91F16"

    def __str__(self):
        return str(self.value)
