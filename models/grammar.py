from shapely.geometry import Polygon
class Grammar:
    def __init__(self, shapes, rules, initial_shape):
        self.shapes = shapes
        self.rules = rules
        self.initial_shape = initial_shape


class Shape:
    def __init__(self, geometry: Polygon, shape_type: str, adjacent_shapes: list):
        self.geometry = geometry
        self.shape_type = shape_type
        self.adjacent_shapes = adjacent_shapes


class Rule:
    def __init__(self, left_side, right_side, condition):
        self.left_side = left_side
        self.right_side = right_side
        self.condition = condition

    def detect_shape(self, shape: Shape, current_shapes: list):
        if (shape.shape_type == self.left_side) and self.condition(shape, current_shapes):
            return True
        return False

    def apply_rule(self, shape: Shape, current_shapes: list):
        return self.right_side(shape, current_shapes)
  
