import numpy as np


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
    def __init__(self, height, width, background_color=Color(0, 0, 0)):
        # default background color is black
        self.height = height
        self.width = width
        self.background_color = background_color.cv_color

    @classmethod
    def from_dict(cls, ranges_dictionary, *background_color):
        width = int(np.ciel(abs(ranges_dictionary['x_range'][1] - ranges_dictionary['x_range'][0])))
        height = int(np.ciel(abs(ranges_dictionary['y_range'][1] - ranges_dictionary['y_range'][0])))
        return cls(height, width, *background_color)
