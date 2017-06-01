__author__ = 'Sidd'

from scipy.optimize import minimize

# minimize x1x4(x1 + x2 + x3) + x3 s.t.
# x1 * x2 * x3 * x4 >= 25 --> constraint 1
# x1^2 + x2^2 + x3^2 + x4^2 = 40 --> constraint 2
# 1 <= x1,x2,x3,x4 <= 5 range for the four vars
# x0 = (1, 5, 5, 1)


# minimize this x1x4(x1 + x2 + x3) + x3
def min_this(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1 * x4 * (x1 + x2 + x3) + x3


def constraint_1(x):
    return x[0] * x[1] * x[2] * x[3] - 25


def constraint_2(x):
    sum_of_square = 40
    for i in range(4):
        sum_of_square -= x[i] ** 2
    return sum_of_square

x0 = [1, 5, 5, 1]  # init x0 guesses from the problem
print min_this(x0)

b = (1.0, 5.0)
bounds_of_problem = (b, b, b, b)
condition_1 = {'type': 'ineq', 'function': constraint_1}
condition_2 = {'type': 'eq', 'function': constraint_2}
conditions = [condition_1, condition_2]

# Sequential Least SQuares Programming
sln = minimize(min_this, x0, method='SLSQP', bounds=bounds_of_problem, constraints=conditions)

print(sln.x)
