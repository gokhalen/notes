# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:48:24 2022

@author: User
"""


import numpy as np
from scipy.optimize import minimize, LinearConstraint


# solve SVM problem with only two data points
# X1=(0,0) -ve class
# X2=(1,1) +ve class
# We choose X1 to enforce the constraint |(w^T)(X1) + b| = 1
# so we choose our hyperplane as ax + ay  - 1 = 0
# so our w = (a,a)
# so the distance of X1 from the hyperplane is 1/||w||
# and maximizing it is the same as minimizaing 
# (1/2)||w||^2 = (1/2)(2*a*a) = a*a
# the linear constraint is (a+a-1)t_2 > 1  where t_2 = 1 is the sign function 

def func(x):
    return x*x

def jac(x):
    return 2*x

linear_constraint = LinearConstraint([[1]],[1],[np.inf])

x0  = np.asarray([3])

res = minimize(func,x0,method='trust-constr',jac=jac,constraints=[linear_constraint])

# so we get a = 1 which is our line x+y-1=0
print('a=',res['x'])

# Solve the same problem as before 
# but with hyperplane defined by ax+by - 1 = 0
# so we have two variables instead of 1
# our distance is 1/||w|| = 1/sqrt(a^2 + b^2)
# instead of maximizing 1/sqrt(a^2 + b^2) we will minimize 0.5*(a^2 + b^2)
# and our constraints are 
# (a,b)^T X1  - 1  which is satisfied identically
# and the second constraint is |a+b-1|t_2 > 1 where t_2 is the sign function
#                              a+b > 2

def func2(x):
    return 0.5*(x[0]*x[0] + x[1]*x[1])

def jac2(x):
    der = np.zeros_like(x)
    der[0] = x[0]
    der[1] = x[1]
    return der

x0_2 = np.asarray([5,5])

linear_constraint2 = LinearConstraint([[1,1]],[2],[np.inf])

res = minimize(func2,x0_2,method='trust-constr',jac=jac2,constraints=[linear_constraint2])

# so we get a=1 and b=1 which is again our line x+y-1=0
print('a= ',res['x'][0],'b= ',res['x'][1])

# Solve the same problem as before 
# but with hyperplane defined by ax+by + c = 0
# so we have 3 variables instead of 2
# our distance is 1/||w|| = 1/sqrt(a^2 + b^2)
# instead of maximizing 1/sqrt(a^2 + b^2) we will minimize 0.5*(a^2 + b^2)
# and our constraints are 
# -((a,b)^T X1 + c) >= 1   ==>  -c>=1  c<=-1
#    (a,b)^T X2 + c >= 1   ===> a+b+c>=1
# 

x0_3 = np.asarray([5.0,5.0,5.0])

def func3(x):
    return 0.5*(x[0]*x[0] + x[1]*x[1])

def jac3(x):
    der = np.zeros_like(x)
    der[0] = x[0]
    der[1] = x[1]
    der[2] = 0
    return der

linear_constraint3 = LinearConstraint([[0,0,1],[1,1,1]],[-np.inf,1],[-1,np.inf])

res = minimize(func3,x0_3,method='trust-constr',jac=jac3,constraints=[linear_constraint3])

print('a= ',res['x'][0],'b= ',res['x'][1],' c= ',res['x'][2])

