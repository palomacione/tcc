from models.grammar import Grammar, Rule, Shape
import random
from shapely.geometry import Polygon, LineString
from shapely.ops import split
from house_grammar import house_grammar
from office_grammar import office_grammar
from utils.plot_utils import plot_shapes

def generate_house_with_house_grammar():
    shape_grammar = house_grammar.create_house_grammar()
    generate_by_shape_grammar(shape_grammar)

def generate_office_with_office_grammar():
    shape_grammar = office_grammar.create_office_grammar()
    generate_by_shape_grammar(shape_grammar)

def pick_random_rule(rules: list):
    return random.choice(rules)

def generate_by_shape_grammar(shape_grammar: Grammar):
    has_rules_to_apply = True
    # The current shape is formed by a set of smaller shapes that form it
    current_shape = [shape_grammar.initial_shape]
    while has_rules_to_apply:
        possible_rules = []
        for shape in current_shape:
            for rule in shape_grammar.rules:
                if rule.detect_shape(shape, current_shape):
                    possible_rules.append({"shape": shape, "rule": rule})
        if len(possible_rules) >= 1:
            picked_rule = pick_random_rule(possible_rules)
            for key, value in picked_rule.items():
                if key == "shape":
                    shape_variable = value
                elif key == "rule":
                    rule_variable = value
            # Transform shape
            new_shape = rule_variable.apply_rule(shape_variable, current_shape)
            current_shape.extend(new_shape)
        else:
            has_rules_to_apply = False
    plot_shapes(current_shape)

generate_office_with_office_grammar()
