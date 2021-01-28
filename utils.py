import re


def point_or_circle(shape):
    if 'radius' in shape.__dict__:
        return True


def remove_number_suffix(string):
    return re.sub(r'_\d+$', '', string)
