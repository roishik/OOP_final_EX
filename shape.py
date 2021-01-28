from image import *
from utils import *
import numpy as np


class Center:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:
    def __init__(self, line_color, fill_color):
        self.line_color = line_color
        self.fill_color = fill_color

    def translate(self, x_translation, y_translation):
        for p in self.points:
            p.x += x_translation
            p.y += y_translation

    def resize(self, scale):
        if point_or_circle(self):
            self.radius *= scale
        else:
            for p in self.points:
                new_x = scale * (p.x - self.center.x) + self.center.x
                new_y = scale * (p.y - self.center.y) + self.center.y
                p.x, p.y = new_x, new_y

    def rotate(self, degrees, radians=False):
        if not point_or_circle(self):
            if radians:
                rad = degrees
            else:
                rad = degrees * np.pi / 180
            for p in self.points:
                x_centered = p.x - self.center.x
                y_centered = p.y - self.center.y
                nex_x_centered = x_centered * np.cos(rad) - y_centered * np.sin(rad)
                new_y_centered = y_centered * np.cos(rad) + x_centered * np.sin(rad)
                new_x = nex_x_centered + self.center.x
                new_y = new_y_centered + self.center.y
                p.x, p.y = new_x, new_y

    @property
    def center(self):
        x_center, y_center = np.mean([(p.x, p.y) for p in self.points], axis=0)
        return Point(x_center, y_center)

    @property
    def bounding_box(self):
        x_max, y_max = np.max([(p.x, p.y) for p in self.points], axis=0)
        x_min, y_min = np.min([(p.x, p.y) for p in self.points], axis=0)
        return {'x_range': [x_min, x_max], 'y_range': [y_min, y_max]}

    @property
    def points(self):
        if self.shape_name == 'point':
            return self
        # get all points in shape
        points_list = []
        for att_name in (att_dict := self.__dict__):
            if att_dict[att_name].shape_name == 'point':
                points_list.append(att_dict[att_name])
            if isinstance(att_dict[att_name], Shape): # recursive for shape with shapes
                points_list.extend(att_dict[att_name].points)
        return points_list
