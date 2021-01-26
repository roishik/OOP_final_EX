class Color():
    def __init__(self, red, green, blue):
        self.r, self.g, self.b = red, green, blue

    @classmethod
    def from_vector(cls, color):
        return cls(color[0], color[1], color[2])

class Shape():
    def __init__(self, line_color, fill_color):
        self.line_color = line_color
        self.fill_color = fill_color
