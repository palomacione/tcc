from models.grammar import Grammar, Rule, Shape
from shapely.geometry import Polygon, LineString
from office_grammar.rules import Rule1, Rule2, Rule3, Rule4, Rule5, Rule6, Rule7, Rule8, Rule9, Rule12, Rule13

def create_office_grammar():
    # Initial shape -> Lot shape
    initial_shape = Shape(Polygon([(0, 0), (0, 5), (10, 5), (10, 0)]), "Espaço", [])

    # Define rules
    rule_1 = Rule1()
    rule_2 = Rule2()
    rule_3 = Rule3()
    rule_4 = Rule4()
    rule_5 = Rule5()
    rule_6 = Rule6()
    rule_7 = Rule7()
    rule_8 = Rule8()
    rule_9 = Rule9()
    rule_12 = Rule12()
    rule_13 = Rule13()
    shape_grammar = Grammar([], [rule_2, rule_3, rule_4, rule_5, rule_6, rule_7, rule_8, rule_9, rule_12, rule_13], initial_shape)
    
    return shape_grammar
