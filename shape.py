from basic_shapes import Point
import numpy as np

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

    def move(self, x_translation, y_translation):
        for p in self.points:
            p.x += x_translation
            p.y += y_translation

    @property
    def center(self):
        x_center, y_center = np.mean([(p.x, p.y) for p in self.points], axis=0)
        return Point(x_center, y_center)

    @property
    def points(self):
        if isinstance(self, Point):
            return self
        # get all points in shape
        points_list = []
        for att_name in (att_dict := self.__dict__):
            if isinstance(att_dict[att_name], Point):
                points_list.append(att_dict[att_name])
            if isinstance(att_dict[att_name], Shape): # recursive for shape with shapes
                points_list.extend(att_dict[att_name].points)
        return points_list
