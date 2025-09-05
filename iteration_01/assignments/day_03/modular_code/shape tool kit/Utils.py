def larger_shape(shape1, shape2):
    if shape1 > shape2:
        return shape1
    else:
        return shape2
    
def convert_unit(x: float) -> float:
    return x*10000
    # Converts from square meters to square centimeters