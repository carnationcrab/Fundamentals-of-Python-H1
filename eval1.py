# SAM MARTORANA

# ################################# [H1_2] ################################# #
# In HTT2 Exercise 2, the parenthesized expression
# 2 - (3 - 1) * 10 / 5 * (2 + 3)
# is given.  This chapter describes the order in which Python evaluates the
# different sub-expressions within it, leading to a single value when Python
# evaluates the entire expression.  
#
# Write a program which breaks this expression down into a series of assignment
# statements, each of the form var = e1 op e2, where
# (a) var is some new variable (a temp variable);
# (b) op is one of the arithmetic operators +,-,/,* and
# (c) each of e1 and e2 is either an int literal or else a temp variable you
# assigned to in earlier statements.
#
# Your final assignment statement should be of the form result = e1 op e2.  
# Note that each of your assignment statements should have only ONE operator
# and TWO operands on the right-hand side.
#
# After this, add the two print statements print(result) and
# print(2-(3-1)*10/5*(2+3)).
#
# Be sure you evaluate the sub-expressions in the correct order when
# calculating result, so that the output of both is the exactly the same.
# Note that 47 is NOT the same as 47.0!
# ########################################################################## #

# # # Evaluate the Parentheses # # #

step1_1 = 3 - 1 # 2
step1_2 = 2 + 3 # 5

step1_result = 2 - (step1_1) * 10 / 5 * (step1_2)

# print('step1_result', step1_result)

# # # Multiplication and division, left to right # # #

step2_1 = step1_1 * 10      # 2 * 10 = 20
step2_2 = step2_1 / 5       # 20 / 5 = 4
step2_3 = step2_2 * step1_2 # 4 * 5 = 20

step2_result = 2 - step2_3

# print('step2_result', step2_result)

# # # subtraction # # #

step3 = 2 - step2_3

result = step3

# # # Print Result # # #

print('result:', step3)

# # # Print Original # # #

origExp = 2 - (3 - 1) * 10 / 5 * (2 + 3)
print('origExp:', origExp)
