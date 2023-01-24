# -*- coding: utf-8 -*-

"""
A factory produces two types of water guns.
Let the weekly capacity be 1200 kilograms of plastic, that is, we can use up to 1200 kilograms of plastic.
And we work not to exceed 40 hours in total per week.
And we need to produce at most 800 dozen per week (two types of pistols)
The Space Rays pistol should not exceed the Zapper pistol production by more than 450 dozen.

Space Rays costs $8 a dozen.
Zapper's profitability is $5 a dozen.

2 kilos of plastic is used for Space Rays and 1 kilo of plastic is used for Zapper per dozen.

Production time per dozen is 3min for Space Rays and 4min for Zapper.

550 dozen Space Rays and 100 dozen Zappers are produced weekly.

Let's optimize the best plan to save money.

X1 = the amount to be produced weekly for Space Rays.
X2 = The amount to be produced weekly for the Zapper.

Objective function, Z = Getting the maximum profit.

#---Objective Function---#
Z = 8*X1 + 5*X2

#---Limitations---#
1- Weekly plastic use should not exceed 1200 kilos.
   2*X1 + 1*X2 <=1200 #2kg X1, 1kg X2

2- Weekly production time 2400 min.
   3*X1 + 4*X2 <=2400 #3dk X1, 4dk X2
   
3- Maximum number of dozen
   X1 + X2 <=800
   
4- The difference between Space Rays and Zapper should not be greater than 450
   X1 <= X2 + 450, X1 - X2 <= 450
   
5- Values cannot be negative
   X1, X2 >= 0
"""

#---------------LIBRARY------------#
#----------------------------------#
import pulp as p

#-----------------CODES-------------#
#-----------------------------------#
#Problem definition
Lp_problem = p.LpProblem('Problem', p.LpMaximize)#We defined the problem as a maximizing problem.

# X1 ve X2
X1 = p.LpVariable('X1', lowBound=0, cat="Integer")
X2 = p.LpVariable('X2', lowBound=0, cat="Integer")#We have defined X1 and X2 variables.

#Objective funciton
Lp_problem += 8*X1 + 5*X2

#Limitations
Lp_problem += 2*X1 + 1*X2 <=1200# kısıt 1
Lp_problem += 3*X1 + 4*X2 <=2400# kısıt 2
Lp_problem += X1 + X2 <=800# kısıt 3
Lp_problem += X1 - X2 <= 450# kısıt 4

print(Lp_problem)#Let's see problem.

solution = Lp_problem.solve()#Solves the problem and transfers it to the solution variable.
print(p.LpStatus[solution])

print('X1', p.value(X1))#Let's see X1 value.
print('X2', p.value(X2))#Let's see X2 value.
print('AMAÇ', p.value(Lp_problem.objective))#Let's see the maximized value of the objective function.

