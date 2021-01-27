from shape import *


class CompoundShape(Shape):
    def __init__(self):
        shapes_list = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes_list.append(shape)
        else:
            raise ValueError(f"shape must be a Shape instance, but {type(shape)} was received")