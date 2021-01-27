from shape import *
import numpy as np
import cv2 as cv

DEFAULT_LINE_WIDTH = 5


class Point(Shape):
    DEFAULT_POINT_SIZE = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = self.DEFAULT_POINT_SIZE

    def draw(self, img):
        drawing_params = {'canvas': img,
                          'center': self.as_tuple,
                          'radius': self.DEFAULT_POINT_SIZE}
        cv.circle(*drawing_params.values(), self.fill_color.cv_color, -1)  # plot shape
        cv.circle(*drawing_params.values(), self.line_color.cv_color, DEFAULT_LINE_WIDTH)  # plot line

    @property
    def as_tuple(self):
        return tuple([self.x, self.y])


class Line(Shape):
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, img):
        drawing_params = {'canvas': img,
                          'point1': self.point_1.as_tuple,
                          'point2': self.point_2.as_tuple}
        cv.line(*drawing_params.values(), self.line_color.cv_color, thickness=DEFAULT_LINE_WIDTH)


class Triangle(Shape):
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def draw(self, img):
        Line(self.point_1, self.point_2).draw(img)
        Line(self.point_1, self.point_3).draw(img)
        Line(self.point_2, self.point_3).draw(img)
        drawing_params = {'canvas': img,
                          'points': [self.point_1.as_tuple, self.point_2.as_tuple, self.point_3.as_tuple]}
        cv.drawContours(*drawing_params.values(), 0, self.fill_color.cv_color, -1)


class Rectangle(Shape):
    def __init__(self, top_left_point, bottom_right_point):
        self.top_left_point = top_left_point
        self.bottom_right_point = bottom_right_point
        self.bottom_left_point = Point(top_left_point.x, bottom_right_point.y)
        self.top_right_point = Point(bottom_right_point.x, top_left_point.y)

    def draw(self, img):
        drawing_params = {'canvas': img,
                          'point1': self.top_left_point.as_tuple,
                          'point2': self.bottom_right_point.as_tuple}
        cv.rectangle(*drawing_params.values(), self.fill_color.cv_color, -1)  # plot shape
        cv.rectangle(*drawing_params.values(), self.line_color.cv_color, DEFAULT_LINE_WIDTH)  # plot line


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = Point(center[0], center[1])
        self.radius = radius

    def draw(self, img):
        drawing_params = {'canvas': img,
                          'center': self.center.as_tuple,
                          'radius': self.radius}
        cv.circle(*drawing_params.values(), self.fill_color.cv_color, -1)  # plot shape
        cv.circle(*drawing_params.values(), self.line_color.cv_color, DEFAULT_LINE_WIDTH)  # plot line
