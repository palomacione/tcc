from models.grammar import Rule, Shape
from shapely.geometry import Polygon
from utils.rules_utils import find_adjacent_shape
from utils import polygon_utils

class Rule1(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_horizontal(shape_geometry)
        escritorios = Shape(splitted[0], "Escritórios", [])
        convivencia = Shape(splitted[1], "Convivência", [])
        return [escritorios, convivencia]

    def condition(self, shape: Shape, current_shapes: list):
        return True
    
    def __init__(self):
        super().__init__("Espaço", self.right_side_function, self.condition)

class Rule2(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_vertical(shape_geometry)
        escritorios = Shape(splitted[0], "Escritórios", [])
        convivencia = Shape(splitted[1], "Convivência", [])
        return [escritorios, convivencia]

    def condition(self, shape: Shape, current_shapes: list):
        return True
    
    def __init__(self):
        super().__init__("Espaço", self.right_side_function, self.condition)

class Rule3(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_horizontal(shape_geometry)
        sala1 = Shape(splitted[1], "Sala", shape.adjacent_shapes)
        sala2 = Shape(splitted[0], "Sala", shape.adjacent_shapes)
        return [sala1, sala2]

    def condition(self, shape: Shape, current_shapes: list):
        return True
        
    def __init__(self):
        super().__init__("Escritórios", self.right_side_function, self.condition)


class Rule4(Rule):

    def right_side_function(self, shape: Polygon, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_quarter_horizontal_top(shape_geometry)
        sala1 = Shape(splitted[1], "Sala", [])
        sala2 = Shape(splitted[0], "Sala", [])
        return [sala1, sala2]

    def condition(self, shape: Shape, current_shapes: list):
        return True
        
    def __init__(self):
        super().__init__("Escritórios", self.right_side_function, self.condition)


class Rule5(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_by_corner_square_right_eight(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            sala = Shape(splitted[0], "Sala", shape.adjacent_shapes)
            banheiro = Shape(splitted[1], "Banheiro", shape.adjacent_shapes)
        else:
            sala = Shape(splitted[1], "Sala", shape.adjacent_shapes)
            banheiro = Shape(splitted[0], "Banheiro", shape.adjacent_shapes)
        sala.adjacent_shapes.append(banheiro)
        return [sala, banheiro]
    
        # Only adds bathroom if shape its not already adjascent to one
    def condition(self, shape: Shape, current_shapes: list):
        for ad_shape in shape.adjacent_shapes:
            if ad_shape.shape_type == "Banheiro":
                return False
        return True

    def __init__(self):
        super().__init__("Sala", self.right_side_function, self.condition)

class Rule6(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_quarter_horizontal_top(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            sala = Shape(splitted[0], "Sala de reuniões", shape.adjacent_shapes)
            copa = Shape(splitted[1], "Copa", shape.adjacent_shapes)
        else:
            sala = Shape(splitted[1], "Sala de reuniões", shape.adjacent_shapes)
            copa = Shape(splitted[0], "Copa", shape.adjacent_shapes)
        return [copa, sala]
    
    def condition(self, shape: Polygon, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Convivência", self.right_side_function, self.condition)

class Rule7(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_quarter_horizontal_bottom(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            sala = Shape(splitted[0], "Sala de reuniões", shape.adjacent_shapes)
            copa = Shape(splitted[1], "Copa", shape.adjacent_shapes)
        else:
            sala = Shape(splitted[1], "Sala de reuniões", shape.adjacent_shapes)
            copa = Shape(splitted[0], "Copa", shape.adjacent_shapes)
        return [copa, sala]
    
    def condition(self, shape: Polygon, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Convivência", self.right_side_function, self.condition)


class Rule8(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_by_corner_square_right_eight(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            copa = Shape(splitted[0], "Copa", shape.adjacent_shapes)
            banheiro = Shape(splitted[1], "Banheiro", shape.adjacent_shapes)
        else:
            copa = Shape(splitted[1], "Copa", shape.adjacent_shapes)
            banheiro = Shape(splitted[0], "Banheiro", shape.adjacent_shapes)
        copa.adjacent_shapes.append(banheiro)
        return [copa, banheiro]
    
    # Only adds bathroom if shape its not already adjascent to one
    def condition(self, shape: Shape, current_shapes: list):
        for ad_shape in shape.adjacent_shapes:
            if ad_shape.shape_type == "Banheiro":
                return False
        return True

    def __init__(self):
        super().__init__("Copa", self.right_side_function, self.condition)

class Rule9(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_quarter_vertical_right(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            sala = Shape(splitted[0], "Sala de reuniões", shape.adjacent_shapes)
            copa = Shape(splitted[1], "Copa", shape.adjacent_shapes)
        else:
            sala = Shape(splitted[1], "Sala de reuniões", shape.adjacent_shapes)
            copa = Shape(splitted[0], "Copa", shape.adjacent_shapes)
        return [copa, sala]
    
    def condition(self, shape: Polygon, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Convivência", self.right_side_function, self.condition)

class Rule12(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_vertical(shape_geometry)
        sala1 = Shape(splitted[1], "Sala", shape.adjacent_shapes)
        sala2 = Shape(splitted[0], "Sala", shape.adjacent_shapes)
        return [sala1, sala2]
    
    def condition(self, shape: Polygon, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Escritórios", self.right_side_function, self.condition)

class Rule13(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_by_corner_square_left_quarter(shape_geometry)

        sala = Shape(splitted[0], "Sala de descanso", shape.adjacent_shapes)
        copa = Shape(splitted[1], "Sala de reuniões", shape.adjacent_shapes)
        return [sala, copa]

    # Only adds bathroom if shape its not already adjascent to one
    def condition(self, shape: Shape, current_shapes: list):
        for shape in current_shapes:
            if shape.shape_type == "Sala de descanso":
                return False
        return True
        
    def __init__(self):
        super().__init__("Sala de reuniões", self.right_side_function, self.condition)
