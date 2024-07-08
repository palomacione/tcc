from models.grammar import Grammar, Rule, Shape
from shapely.geometry import Polygon, LineString
from house_grammar.rules import Rule1, Rule2, Rule3, Rule4, Rule5, Rule6, Rule7, Rule8, Rule9, Rule10, Rule11, Rule12, Rule13, Rule14, Rule15, Rule16, Rule17, Rule18, Rule19
def create_house_grammar():
    # Forma Inicial
    initial_shape = Shape(Polygon([(0, 0), (0, 15), (10, 15), (10, 0)]), "Espaço", [])

    # Regras
    rule_1 = Rule1()
    rule_2 = Rule2()
    rule_3 = Rule3()
    rule_4 = Rule4()
    rule_6 = Rule6()
    rule_5 = Rule5()
    rule_7 = Rule7()
    rule_8 = Rule8()
    rule_9 = Rule9()
    rule_10 = Rule10()
    rule_11 = Rule11()
    rule_12 = Rule12()
    rule_13 = Rule13()
    rule_14 = Rule14()
    rule_15 = Rule15()
    rule_16 = Rule16()
    rule_17 = Rule17()
    rule_18 = Rule18()
    rule_19 = Rule19()
    shape_grammar = Grammar([], [rule_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule_7, rule_8, rule_9, rule_10, rule_11, rule_12, rule_13, rule_14, rule_15, rule_16, rule_17, rule_18, rule_19], initial_shape)
    
    return shape_grammar
