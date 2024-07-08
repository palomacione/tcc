from models.grammar import Grammar, Rule, Shape
from shapely.geometry import Polygon, LineString
from shapely.ops import split

def split_vertical(shape):
    min_x, min_y, max_x, max_y = shape.bounds
    mid_x = (min_x + max_x) / 2

    split_line = LineString([(mid_x, min_y), (mid_x, max_y)])

    return split(shape, split_line).geoms


def split_horizontal(shape):
    min_x, min_y, max_x, max_y = shape.bounds
    mid_y = (min_y + max_y) / 2
    split_line = LineString([(min_x, mid_y), (max_x, mid_y)])
    return split(shape, split_line).geoms

def split_horizontal_three_quarters(shape):
    min_x, min_y, max_x, max_y = shape.bounds
    mid_y = (min_y + max_y) / 3
    
    split_line = LineString([(min_x, mid_y), (max_x, mid_y)])
    return split(shape, split_line).geoms

def split_quarter_horizontal_bottom(shape):
    min_x, min_y, max_x, max_y = shape.bounds

    altura = max_y - min_y
    y_quarto = altura / 4

    linha_divisao = LineString([(min_x, min_y + y_quarto), (max_x, min_y + y_quarto)])

    return split(shape, linha_divisao).geoms

def split_quarter_horizontal_top(shape):
    min_x, min_y, max_x, max_y = shape.bounds

    altura = max_y - min_y
    y_quarto = altura / 4

    linha_divisao = LineString([(min_x, max_y - y_quarto), (max_x, max_y - y_quarto)])

    return split(shape, linha_divisao).geoms

def split_eight_horizontal_top(shape):
    min_x, min_y, max_x, max_y = shape.bounds

    altura = max_y - min_y
    y_quarto = altura / 8

    linha_divisao = LineString([(min_x, max_y - y_quarto), (max_x, max_y - y_quarto)])

    return split(shape, linha_divisao).geoms

def split_eight_horizontal_bottom(shape):
    min_x, min_y, max_x, max_y = shape.bounds

    altura = max_y - min_y
    y_quarto = altura / 8

    linha_divisao = LineString([(min_x, min_y + y_quarto), (max_x, min_y + y_quarto)])

    return split(shape, linha_divisao).geoms

def split_quarter_vertical_left(shape):
    min_x, min_y, max_x, max_y = shape.bounds

    largura = max_x - min_x
    x_quarto = largura / 4

    linha_divisao = LineString([(min_x + x_quarto, min_y), (min_x + x_quarto, max_y)])
    return split(shape, linha_divisao).geoms

def split_quarter_vertical_right(shape):
    min_x, min_y, max_x, max_y = shape.bounds

    largura = max_x - min_x
    x_quarto = largura / 4

    linha_divisao = LineString([(max_x - x_quarto, min_y), (max_x - x_quarto, max_y)])
    return split(shape, linha_divisao).geoms

def get_rightmost_point(polygon):
    max_x = max(polygon.exterior.coords, key=lambda point: point[0])[0]
    rightmost_points = [point for point in polygon.exterior.coords if point[0] == max_x]
    rightmost_point = max(rightmost_points, key=lambda point: point[1])
    return rightmost_point

def get_leftmost_point(polygon):
    min_x = min(polygon.exterior.coords, key=lambda point: point[0])[0]
    leftmost_points = [point for point in polygon.exterior.coords if point[0] == min_x]
    leftmost_point = min(leftmost_points, key=lambda point: point[1])
    return leftmost_point

def create_square_with_area(bottom_left_point, area):
    side_length = area**0.5
    bottom_left_x, bottom_left_y = bottom_left_point
    square_coords = [
        (bottom_left_x, bottom_left_y),
        (bottom_left_x + side_length, bottom_left_y),
        (bottom_left_x + side_length, bottom_left_y + side_length),
        (bottom_left_x, bottom_left_y + side_length)
    ]
    return Polygon(square_coords), side_length

def split_by_corner_square_right_eight(shape):
    polygon_area = shape.area
    small_square_area = polygon_area / 8
    rightmost_point = get_rightmost_point(shape)

    bottom_left_x = min(rightmost_point[0], shape.bounds[2] - (small_square_area**0.5))
    bottom_left_y = min(rightmost_point[1], shape.bounds[3] - (small_square_area**0.5))

    small_square, side_length = create_square_with_area((bottom_left_x, bottom_left_y), small_square_area)

    remaining_polygon = shape.difference(small_square)
    return [small_square, remaining_polygon]


def split_by_corner_square_left_quarter(shape):
    polygon_area = shape.area
    small_square_area = polygon_area / 4

    leftmost_point = get_leftmost_point(shape)
    bottom_left_x = leftmost_point[0]
    bottom_left_y = min(leftmost_point[1], shape.bounds[3] - (small_square_area**0.5))
    small_square, side_length = create_square_with_area((bottom_left_x, bottom_left_y), small_square_area)

    remaining_polygon = shape.difference(small_square)
    return [small_square, remaining_polygon]
