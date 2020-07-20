# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:48:06 2020

@author: aa
"""

# https://github.com/numpy/numpy/issues/16885

'''
Thanks for raising, this is indeed a bit hairy. The more detailed documentation on advanced indexing in the reference guide describes what's happening here. Essentially, Boolean indexing works like advanced indexing with integer arrays constructed from mask.nonzero(). This works as expected when there is a single indexing mask but, as you note, might result in different behavior than expected when trying to use multiple masks along different axes.

To illustrate:

>>> b1.nonzero()
(array([1, 2]),)
>>> b2.nonzero()
(array([0, 2]),)
>>> a[b1.nonzero(), b2.nonzero()]
array([[ 4, 10]])
The only reason a[b1, b2] works at all in the quickstart tutorial is because b1 and b2 both have the same number of True elements (2). This also explains why your all-true masks example fails (try applying the "advanced indexing with integer arrays" rules with array([0, 1, 2]) and array([0, 1, 2, 3])).

Re: the quickstart tutorial - maybe stronger wording and a link to the relevant section of the reference guide would help clear this up (perhaps a fix-up to the linked cookbook article as well!). Suggestions welcome!
'''