from shape import *
from basic_shapes import *
from compund_shape import *
from utils import *


basic_shapes_names_and_classes = ['point', 'line', 'triangle', 'rectangle', 'circle']


def class_instance_from_name(class_name, *prop):
    if class_name == 'point':
        return Point(*prop)
    elif class_name == 'line':
        return Line(*prop)
    elif class_name == 'triangle':
        return Triangle(*prop)
    elif class_name == 'rectangle':
        return Rectangle(*prop)
    elif class_name == 'circle':
        return Circle(*prop)


def name_from_class_instance(class_instance):
    if isinstance(class_instance, Point):
        return 'point'
    elif isinstance(class_instance, Line):
        return 'line'
    elif isinstance(class_instance, Triangle):
        return 'triangle'
    elif isinstance(class_instance, Rectangle):
        return 'rectangle'
    elif isinstance(class_instance, Circle):
        return 'circle'
    elif isinstance(class_instance, CompoundShape):
        return 'compound_shape'
    else:
        raise ValueError(f"{class_instance} is not an instance of one of the known classes.")


def dict_to_compound_shape(shape_dictionary):
    compound_shape = CompoundShape()
    for shape_key, shape_prop in shape_dictionary:
        shape_name = remove_number_suffix(shape_key)
        if shape_name in basic_shapes_names_and_classes:
            compound_shape.add_shape(class_instance_from_name(shape_name, *shape_prop.valus()))
        elif shape_name == 'compound_shape':
            return dict_to_compound_shape(shape_prop)
        else:
            raise ValueError(f"Shape keys must be one of the shape names: {basic_shapes_names_and_classes} "
                             f"or 'compound_shape', suffixed by _(serial-number)."
                             f"Instead, {shape_key} was received.")


def shape_to_dict(shape):
    key = name_from_class_instance(shape)
    
