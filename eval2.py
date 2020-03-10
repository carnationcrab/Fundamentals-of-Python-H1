# SAM MARTORANA

# ################################# [H1_3] ################################# #
# Same as the previous, but for the expression:
# 1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4.
# Note the use of the two operators ** (exponentiation) and //
# (integer division). Also note a**b**c is evaluated right-to-left, equivalent
# to the parenthesized expression a**(b**c).  ** is the only such
# right-to-left operator; all other equivalent precedence operators evaluate
# left-to-right: 1+2-3 is equivalent to (1+2)-3.
# ########################################################################## #

# # # Evaluate the Exponents # # #

step1_1 = 3 ** 2 # 8
step1_2 = 2 ** step1_1 # 512

step1_result = 1.0 + 2.0 * step1_2 % 3 - 6 // 4

# # # Multiplication and division, left to right # # #

step2_1 = 2.0 * step1_2     # 2 * 512 = 1024.0
step2_2 = step2_1 % 3       # 1024.0 % 3 = 1.0
step2_3 = 6 // 4            # 1

# # # subtraction and addition # # #

step3_1 = 1.0 + step2_2
step3_2 = step3_1 - step2_3

result = step3_2

# # # Print Result # # #

print('result:', step3_2)

# # # Print Original # # #

origExp = 1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4
print('origExp:', origExp)
