class Color():
    def __init__(self, red, green, blue):
        self.r, self.g, self.b = red, green, blue

    @property
    def cv_color(self):
        # openCV uses BGR color map, instead of rgb
        return self.b, self.g, self.r

    @classmethod
    def from_vector(cls, color):
        return cls(color[0], color[1], color[2])


class Img:
    def __init__(self, height, length, background_color=Color(0, 0, 0)):
        # default background color is black
        self.height = height
        self.length = length
        self.background_color = background_color

    def draw(self):
        pass
