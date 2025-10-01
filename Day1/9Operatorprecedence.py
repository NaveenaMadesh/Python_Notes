P = 2; Q=3; R=4
X = P *2 + Q - 2 + R-2
print(X)

'''Python follows: PEMDAS/BODMAS
'''
# 1.Parentheses ()-->Higher priority
# 2.Exponentation **
# 3.Multiplication,Division,Floor Division,Modulus *,/,//,%
# 4.Addition,Subtraction +,-(left to right)
# 5.Assignment = Lowest priority

'''PriorityOperatorDescriptionExample1 (Highest)()Parentheses(2 + 3)2**Exponentiation2 ** 33+x, -x, ~xUnary plus, minus, NOT-54*, /, //, %Multiply, Divide, Floor div, Modulus5 * 25+, -Addition, Subtraction5 + 26<<, >>Bitwise shiftsx << 27&Bitwise ANDx & y8^Bitwise XORx ^ y9|Bitwise ORx | y10==, !=, >, <, >=, <=Comparisonsx == y11notLogical NOTnot x12andLogical ANDx and y13orLogical ORx or y14 (Lowest)=, +=, -=, etc.Assignmentx = 5'''