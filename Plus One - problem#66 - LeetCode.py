'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''

# class Solution(object):
#     def plusOne(self, digits):
#         if len(digits)==2 and digits[-2]==9:
#             if digits[-2] == 9:
#                 del digits[-1]
#                 del digits[-1]
#                 digits.append(1)
#                 digits.append(0)
#                 digits.append(0)
#         elif digits[-1] == 9:
#             del digits[-1]
#             digits.append(1)
#             digits.append(0)
#         else:
#             digits[-1] = digits[-1] + 1
#         print(digits)
#         return digits

# digits =[9]
# Solution().plusOne(digits)

class Solution(object):
    def plusOne(self, digits):
        digits=str(int(''.join([str(x) for x in digits]))+1)
        ret=[]
        for i in range(len(digits)):
            ret.append(int(digits[i:i+1]))
        return ret

#RunTime: 4ms ( a lot better than mine(26ms) )
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #https://www.youtube.com/watch?v=G737jzcxG9A
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        return [1] + digits

# Memory Usage: 13K MB
class Solution(object):
    def plusOne(self, digits):
        num = ""
        for i in digits:
            num += str(i)
        num = int(num)+1
        num = str(num)
        return [int(i) for i in num]
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].


Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""