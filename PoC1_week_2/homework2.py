import math

'''
Consider the following Python function:
'''
def root (a, b, c):
    discriminant = b ** 2 - 4 * a * c
    return (-b - discriminant ** 0.5) / (2 * a)
'''
1. Which mathematical function below computes the same value as this function?
'''

# root(a, b, c) = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)

'''
2.
Which of the mathematical functions displayed below are linear?
f(x)=x+10
h(z)=3
b(y)=(y+1)/(y-1)
c(z)=z**0.5
g(y)=2y-3
'''
# f(x)=x+10
# h(z)=3
# g(y)=2y-3

'''
3.
Compute the logarithm base 5 of (5**7)**.5 which corresponds to the value of the mathematical
expression log5((5**7)**.5). Enter the answer the box below in decimal form.
'''
print '---- QUESTION 3 ----'
print math.log((5**7)**.5, 5) # 3.5

'''
4.
How many significant digits does the decimal number 0.00400100 have?
Explanation at Khan Academy:
https://www.khanacademy.org/math/arithmetic-home/arith-review-decimals/arithmetic-significant-figures-tutorial/
'''

print '---- QUESTION 4 ----'


def get_signif_figures(str_number):
    if str_number[0] != '0' and '.' not in str_number:
        return '{} significant digits: {}'.format(len(str_number), str_number)
    else:
        for idx in xrange(len(str_number)):
            if str_number[idx] != '0' and str_number[idx] != '.':
                result = str_number[idx:]
                return '{} significant digits: {}'.format(len(result), result)
print get_signif_figures('0.00400100')
# 6 significant digits: 400100

'''
5.
What is the mantissa for 0.00400100 when expressed in scientific notation?
a=4.00100
a=4.001
a=0.400100
a=0.4001
'''
# a=4.00100
# a=0.400100

'''
6.
For this question, look up (or compute) the decimal representation of the number pi and
enter the value of pi with five significant digits of precision in the box below.
Remember to round as describe above.
'''

print '---- QUESTION 6 ----'

print math.pi # 3.14159265359
print round(math.pi, 4) # 3.1416

'''
7.
Consider the following code snippet:
'''
# row = '...'
# col = '...'
nested_list = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

# print nested_list[row][col]

'''
If running this code snippet prints 13 in the console, what are the non-negative
values of row and col? Enter these two values below as numbers separated by a space.
'''
print '---- QUESTION 7 ----'
for row in xrange(len(nested_list)):
    for col in xrange(len(nested_list[row])):
        if nested_list[row][col] == 13:
            print nested_list[row][col]
            print row, col # 2 3

'''
8.
Review the math notes on Grids. Given a grid of size 4x6, what are the row and column
indices for the upper right cell in this grid? Enter the row and columns indices
below as numbers separated by a space.
'''
print '---- QUESTION 8 ----'
grid = [['x' for x in xrange(6)] for y in xrange(4)]
grid[0][5] = 'O'
for r_o_w in grid:
    print r_o_w
# 0 5

'''
9.
Given a 4x4 grid, what values for start_cell and direction would cause traverse_grid
to traverse the diagonal of grid connecting the lower right tile to the upper left tile?
source code: http://www.codeskulptor.org/#poc_grid_traversal.py
start_cell = (3, 0)
direction = (-1, 0)

start_cell = (0, 0)
direction = (1, 1)

start_cell = (3, 3)
direction = (-1, -1)

start_cell = (3, 0)
direction = (0, 1)
'''
# start_cell = (3, 3)
# direction = (-1, -1)