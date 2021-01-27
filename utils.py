def point_or_circle(shape):
    if 'radius' in shape.__dict__:
        return True
