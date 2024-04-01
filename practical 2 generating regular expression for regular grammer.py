# Aim:- Write a program for generating regular expressions for regular grammar

import re

def generate_regex(grammar):
    regex_rules = {}
    
    for rule in grammar:
        non_terminal, production = rule.split(' -> ')
        if production[0] == production[-1] == "'":
            regex_rules[non_terminal] = production[1:-1]
        elif production == 'ε':
            regex_rules[non_terminal] = ''
        else:
            regex_rules[non_terminal] = production
    
    for non_terminal, regex in regex_rules.items():
        for other_non_terminal in regex_rules:
            regex = re.sub(other_non_terminal, f'({regex_rules[other_non_terminal]})', regex)
        
        regex_rules[non_terminal] = regex
    
    return regex_rules

if __name__ == "__main__":
    regular_grammar = [
        "S -> aS",
        "S -> bA",
        "A -> aB",
        "A -> bS",
        "B -> bB",
        "B -> ε"
    ]
    
    regex_rules = generate_regex(regular_grammar)
    
    print("Regular Expressions:")
    for non_terminal, regex in regex_rules.items():
        print(f"{non_terminal}: {regex}")
