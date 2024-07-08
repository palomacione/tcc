from models.grammar import Rule, Shape
from shapely.geometry import Polygon
from utils.rules_utils import find_adjacent_shape
from utils import polygon_utils

class Rule1(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_eight_horizontal_top(shape_geometry)
        inside = Shape(splitted[0], "Espaço interior", [])
        outside = Shape(splitted[1], "Espaço exterior", [])
        inside.adjacent_shapes.append(outside)
        outside.adjacent_shapes.append(inside)
        return [inside, outside]

    def condition(self, shape: Shape, current_shapes: list):
        return True
    
    def __init__(self):
        super().__init__("Espaço", self.right_side_function, self.condition)

class Rule2(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_eight_horizontal_bottom(shape_geometry)
        inside = Shape(splitted[1], "Espaço interior", [])
        outside = Shape(splitted[0], "Espaço exterior", [])
        inside.adjacent_shapes.append(outside)
        outside.adjacent_shapes.append(inside)
        return [inside, outside]
    
    def condition(self, shape: Shape, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Espaço", self.right_side_function, self.condition)

class Rule3(Rule):

    def right_side_function(self, shape: Polygon, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_vertical(shape_geometry)
        dorms = Shape(splitted[1], "Dormitórios", [])
        living = Shape(splitted[0], "Convivência", [])
        dorms.adjacent_shapes.append(living)
        living.adjacent_shapes.append(dorms)
        return [dorms, living]

    def condition(self, shape: Shape, current_shapes: list):
        return True
        
    def __init__(self):
        super().__init__("Espaço interior", self.right_side_function, self.condition)

class Rule4(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_quarter_vertical_right(shape_geometry)
        
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            living = Shape(splitted[0], "Convivência", [])
            circulation = Shape(splitted[1], "Circulação", [])
        else:
            living = Shape(splitted[1], "Convivência", [])
            circulation = Shape(splitted[0], "Circulação", [])
        living.adjacent_shapes.append(circulation)
        circulation.adjacent_shapes.append(living)
        return [living, circulation]

    # Only adds circulation if shape its not already adjascent to one
    def condition(self, shape: Shape, current_shapes: list):
        for ad_shape in shape.adjacent_shapes:
            if ad_shape.shape_type == "Circulação":
                return False
        return True

    def __init__(self):
        super().__init__("Convivência", self.right_side_function, self.condition)


class Rule5(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry

        splitted = polygon_utils.split_vertical(shape_geometry)
        service = Shape(splitted[1], "Área de serviço", [])
        yard = Shape(splitted[0], "Quintal", [])
        service.adjacent_shapes.append(yard)
        yard.adjacent_shapes.append(service)
        return [service, yard]

    def condition(self, shape: Shape, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Espaço exterior", self.right_side_function, self.condition)

class Rule6(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_horizontal(shape_geometry)
        bedroom1 = Shape(splitted[1], "Quarto", [])
        bedroom2 = Shape(splitted[0], "Quarto", [])
        bedroom1.adjacent_shapes.append(bedroom2)
        bedroom2.adjacent_shapes.append(bedroom1)
        return [bedroom1, bedroom2]

    def condition(self, shape: Polygon, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Dormitórios", self.right_side_function, self.condition)

class Rule7(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        return [Shape(shape.geometry, "Quarto", [])]

    def condition(self, shape: Shape, current_shapes: list):
        return True
    
    def __init__(self):
        super().__init__("Dormitórios", self.right_side_function, self.condition)


class Rule8(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_quarter_horizontal_top(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            bedroom = Shape(splitted[0], "Quarto", shape.adjacent_shapes)
            bathroom = Shape(splitted[1], "Banheiro", shape.adjacent_shapes)
        else:
            bedroom = Shape(splitted[1], "Quarto", shape.adjacent_shapes)
            bathroom = Shape(splitted[0], "Banheiro", shape.adjacent_shapes)
        bedroom.adjacent_shapes.append(bathroom)
        bathroom.adjacent_shapes.append(bedroom)
        return [bedroom, bathroom]
    
        # Only adds bathroom if shape its not already adjascent to one
    def condition(self, shape: Shape, current_shapes: list):
        for ad_shape in shape.adjacent_shapes:
            if ad_shape.shape_type == "Banheiro":
                return False
        return True

    def __init__(self):
        super().__init__("Quarto", self.right_side_function, self.condition)

class Rule9(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_quarter_vertical_right(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            bedroom = Shape(splitted[0], "Quarto", shape.adjacent_shapes)
            storage = Shape(splitted[1], "Closet", shape.adjacent_shapes)
        else:
            bedroom = Shape(splitted[1], "Quarto", shape.adjacent_shapes)
            storage = Shape(splitted[0], "Closet", shape.adjacent_shapes)
        bedroom.adjacent_shapes.append(storage)
        storage.adjacent_shapes.append(bedroom)
        current_shapes.remove(shape)
        return [bedroom, storage]

    # Only adds bathroom if shape its not already adjacent to one
    def condition(self, shape: Shape, current_shapes: list):
        for ad_shape in shape.adjacent_shapes:
            if ad_shape.shape_type == "Closet":
                return False
        return True

    def __init__(self):
        super().__init__("Quarto", self.right_side_function, self.condition)


class Rule10(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_horizontal(shape_geometry)
        kitchen = Shape(splitted[1], "Cozinha", [])
        dining = Shape(splitted[0], "Sala de Estar", [])
        kitchen.adjacent_shapes.append(dining)
        dining.adjacent_shapes.append(kitchen)
        return [dining, kitchen]

    def condition(self, shape: Shape, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Convivência", self.right_side_function, self.condition)

class Rule11(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        return [Shape(shape.geometry, "Varanda", [])]

    def condition(self, shape: Shape, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Espaço exterior", self.right_side_function, self.condition)

class Rule12(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        splitted = polygon_utils.split_by_corner_square_right_eight(shape.geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            kitchen = Shape(splitted[0], "Cozinha", [])
            dining = Shape(splitted[1], "Área de serviço", [])
        else:
            kitchen = Shape(splitted[1], "Cozinha", [])
            dining = Shape(splitted[0], "Área de serviço", [])
        kitchen.adjacent_shapes.append(dining)
        dining.adjacent_shapes.append(kitchen)
        return [kitchen, dining]

    def condition(self, shape: Shape, current_shapes: list):
        for c_shape in current_shapes:
            if c_shape.shape_type == "Área de serviço":
                return False
        return True

    def __init__(self):
        super().__init__("Cozinha", self.right_side_function, self.condition)

class Rule13(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_horizontal(shape_geometry)
        kitchen = Shape(splitted[1], "Sala de Estar", [])
        room = Shape(splitted[0], "Cozinha", [])

        return [kitchen, room]

    def condition(self, shape: Shape, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Convivência", self.right_side_function, self.condition)

class Rule14(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        splitted = polygon_utils.split_eight_horizontal_bottom(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            bedroom = Shape(splitted[0], "Quarto", shape.adjacent_shapes)
            storage = Shape(splitted[1], "Closet", shape.adjacent_shapes)
        else:
            bedroom = Shape(splitted[1], "Quarto", shape.adjacent_shapes)
            storage = Shape(splitted[0], "Closet", shape.adjacent_shapes)
        bedroom.adjacent_shapes.append(storage)
        storage.adjacent_shapes.append(bedroom)
        current_shapes.remove(shape)
        return [bedroom, storage]

    # Only adds bathroom if shape its not already adjacent to one
    def condition(self, shape: Shape, current_shapes: list):
        for ad_shape in shape.adjacent_shapes:
            if ad_shape.shape_type == "Closet":
                return False
        return True

    def __init__(self):
        super().__init__("Quarto", self.right_side_function, self.condition)

class Rule15(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        splitted = polygon_utils.split_by_corner_square_right_eight(shape.geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            kitchen = Shape(splitted[0], "Sala de Estar", [])
            dining = Shape(splitted[1], "Sala de Jantar", [])
        else:
            kitchen = Shape(splitted[1], "Sala de Estar", [])
            dining = Shape(splitted[0], "Sala de Jantar", [])
        kitchen.adjacent_shapes.append(dining)
        dining.adjacent_shapes.append(kitchen)
        return [kitchen, dining]

    def condition(self, shape: Shape, current_shapes: list):
        for c_shape in current_shapes:
            if c_shape.shape_type == "Sala de Jantar":
                return False
        return True

    def __init__(self):
        super().__init__("Sala de Estar", self.right_side_function, self.condition)

class Rule16(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        splitted = polygon_utils.split_by_corner_square_left_quarter(shape.geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            kitchen = Shape(splitted[0], "Sala de Estar", [])
            dining = Shape(splitted[1], "Sala de Jantar", [])
        else:
            kitchen = Shape(splitted[1], "Sala de Estar", [])
            dining = Shape(splitted[0], "Sala de Jantar", [])
        kitchen.adjacent_shapes.append(dining)
        dining.adjacent_shapes.append(kitchen)
        return [kitchen, dining]

    def condition(self, shape: Shape, current_shapes: list):
        for c_shape in current_shapes:
            if c_shape.shape_type == "Sala de Jantar":
                return False
        return True

    def __init__(self):
        super().__init__("Sala de Estar", self.right_side_function, self.condition)

class Rule17(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        splitted = polygon_utils.split_quarter_horizontal_bottom(shape.geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            kitchen = Shape(splitted[0], "Sala de Estar", [])
            dining = Shape(splitted[1], "Sala de Jantar", [])
        else:
            kitchen = Shape(splitted[1], "Sala de Estar", [])
            dining = Shape(splitted[0], "Sala de Jantar", [])
        kitchen.adjacent_shapes.append(dining)
        dining.adjacent_shapes.append(kitchen)
        return [kitchen, dining]

    def condition(self, shape: Shape, current_shapes: list):
        for c_shape in current_shapes:
            if c_shape.shape_type == "Sala de Jantar":
                return False
        return True

    def __init__(self):
        super().__init__("Sala de Estar", self.right_side_function, self.condition)

class Rule18(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        shape_geometry = shape.geometry
        current_shapes.remove(shape)
        splitted = polygon_utils.split_horizontal_three_quarters(shape_geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            bedroom1 = Shape(splitted[0], "Quarto", [])
            bedroom2 = Shape(splitted[1], "Escritório", [])
        else:
            bedroom1 = Shape(splitted[1], "Quarto", [])
            bedroom2 = Shape(splitted[0], "Escritório", [])
        bedroom1.adjacent_shapes.append(bedroom2)
        bedroom2.adjacent_shapes.append(bedroom1)
        return [bedroom1, bedroom2]

    def condition(self, shape: Polygon, current_shapes: list):
        return True

    def __init__(self):
        super().__init__("Dormitórios", self.right_side_function, self.condition)

class Rule19(Rule):

    def right_side_function(self, shape: Shape, current_shapes: list):
        current_shapes.remove(shape)
        splitted = polygon_utils.split_quarter_horizontal_bottom(shape.geometry)
        area_1, area_2 = splitted[0].area, splitted[1].area
        if (area_1 > area_2):
            kitchen = Shape(splitted[0], "Cozinha", shape.adjacent_shapes)
            dining = Shape(splitted[1], "Sala de Jantar", [])
        else:
            kitchen = Shape(splitted[1], "Cozinha", shape.adjacent_shapes)
            dining = Shape(splitted[0], "Sala de Jantar", [])
        kitchen.adjacent_shapes.append(dining)
        dining.adjacent_shapes.append(kitchen)
        return [kitchen, dining]

    def condition(self, shape: Shape, current_shapes: list):
        for c_shape in current_shapes:
            if c_shape.shape_type == "Sala de Jantar":
                return False
        return True

    def __init__(self):
        super().__init__("Cozinha", self.right_side_function, self.condition)
