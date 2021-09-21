# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:32:42 2021

@author: User
"""

# motivated by the case {'foo':bar} 
# https://benhoyt.com/writings/python-pattern-matching/

# lesson 1 seems to need two braces to produce a 
# single brace in the output

# https://stackoverflow.com/questions/42521230/how-to-escape-curly-brackets-in-f-strings
bar = 11
# this is normal -
print(f'{bar}')
# two {{ escape f-string formatting
# so when it sees two {{ it is going to put a single {
# and what's inside that 
print(f'{{bar}}')
# same as before 
# first two {{  means a single brace in the output 
# and what's inside, which is {bar} which evaluates to 11
print(f'{{{bar}}}')
# same as before
# the {{{{ results in {{  in the output plus what is inside
# which is bar
print(f'{{{{bar}}}}')
# same as before
# the {{{{ results in {{  plus what is inside which is {bar}
# which evaluates to 11
print(f'{{{{{bar}}}}}')
# the {{{{{{ results in {{{ plus what is inside which is bar
print(f'{{{{{{bar}}}}}}')

# same logic applies to before
print(f"{{'foo': {bar}}}")
print(f"{{'foo': {{bar}}}}")

# note 
print(f'{{')   # is valid
print(f'{{{')  # is not valid