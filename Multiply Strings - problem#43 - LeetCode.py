'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


# class Solution(object):
#     def multiply(self, num1, num2):
        
#         n1 = float(num1)
#         N1 = int(n1)
#         n2 = float(num2)
#         N2 = int(n2)
#         r_Int = (N1.__floor__()) * (N2.__floor__())
#         r_str = str(r_Int)
#         return r_str
    
class Solution(object):
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))

"""
Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"


Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

"""