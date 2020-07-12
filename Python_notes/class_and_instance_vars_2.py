# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:40:06 2020

@author: Gokhale
"""

# https://diveintopython3.problemsolving.io/iterators.html

class LazyRules:
    rules_filename='plural6-rules.txt'
    
r1 = LazyRules()
r2 = LazyRules()
# when lookup for instance vars fails, class vars are returnd
print(f'r1.rules_filename={r1.rules_filename}')
print(f'r2.rules_filename={r2.rules_filename}')
# when we're not explicitly setting class vars, they are assumed 
# to be instance vars. here a new instance variable, rules_filename 
# is created
r2.rules_filename='r2-override.txt'
# prints instance variable
print(f'r2.rules_filename={r2.rules_filename}')
# prints class variable, because instance var is not def
print(f'r1.rules_filename={r1.rules_filename}')
r2.__class__.rules_filename='papayawhip.txt'
# will print the class variable 'papayawhip.txt'
print(f'r1.rules_filename={r1.rules_filename}')
# will print the instance variable 'r2-override.txt'
print(f'r2.rules_filename={r2.rules_filename}')
# class variable is changed in both places
print(f'r1.rules_filename={r1.__class__.rules_filename}')
print(f'r2.rules_filename={r2.__class__.rules_filename}')
