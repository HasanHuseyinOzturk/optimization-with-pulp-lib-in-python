# -*- coding: utf-8 -*-

"""
Maximizing and minimizing problem solutions using linear regression with pulp.

Objective function, Z= 1200X1 + 2000X2
Limitations, 2X1 + 6X2 <=27
Limitations, X2 >=2
Limitations, 3X1 + X2 <=19
Limitations, X1, X2 >=0 and int
"""

#---------------LIBRARY------------#
#----------------------------------#
import pulp as p

#-----------------CODES-------------#
#-----------------------------------#
Lp_problem = p.LpProblem('Problem', p.LpMaximize)#We have defined problem as a maximizing problem.

X1 = p.LpVariable('X1', lowBound=0, cat="Integer")
X2 = p.LpVariable('X2', lowBound=0, cat="Integer")#We have defined X1 and X2 variables.

Lp_problem += 1200*X1 + 2000*X2#We have defined objective function.

Lp_problem += 2*X1 + 6*X2 <=27#First limitations.
Lp_problem += X2 >=2#Second limitations.
Lp_problem += 3*X1 + X2 <=19#Third limitations.

print(Lp_problem)#Let's see problem.

#----SOLUTION----#
#----------------#
status = Lp_problem.solve()#Solves the problem and transfers it to the state variable.
print(p.LpStatus[status])

print('X1', p.value(X1))#Let's see X1 value.
print('X2', p.value(X2))#Let's see X1 value.
print('AMAÇ', p.value(Lp_problem.objective))#Let's see the maximized value of the objective function.

