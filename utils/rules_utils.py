from models.grammar import Rule, Shape

def find_adjacent_shape(shape_index: int, current_shapes: list, target_shape: str):
    if (shape_index == 0):
        return current_shapes[shape_index + 1].properties["type"] != target_shape
    elif (shape_index == len(current_shapes) - 1):
        return current_shapes[shape_index - 1].properties["type"] != target_shape
    else:
        return (current_shapes[shape_index + 1].properties["type"] == target_shape or current_shapes[shape_index - 1].properties["type"] == target_shape)
