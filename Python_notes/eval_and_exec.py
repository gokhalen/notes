# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:07:01 2021

@author: aa
"""

a1 = 11
a2 = 32

# eval can evaluate expressions in the context of the current namespace
s  = eval('a1')
print(s)

s = eval('a1+a2')
print(s)

# exec can create objects programmatically
# \n and \t seem to stand for indentatation
codestring = "def Nachiket():\n\tprint('Booga Booga')\n\tfor i in range(4):\n\t\tprint(i)\n\tprint('Goodbye')"
print(codestring)

exec(codestring)
Nachiket()
