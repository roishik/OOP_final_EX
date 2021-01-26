import numpy as np
import cv2 as cv


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    @property
    def center(self):
        return Point(np.mean([self.point_1.x, self.point_2.x], np.mean([self.point_1.y, self.point_2.y])))


class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point3 = point_3


class Rectangle:
    def __init__(self, top_left_point, bottom_right_point):
        self.top_left_point = top_left_point
        self.bottom_right_point = bottom_right_point
        self.bottom_left_point = Point(top_left_point.x, bottom_right_point.y)
        self.top_right_point = Point(bottom_right_point.x, top_left_point.y)


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

