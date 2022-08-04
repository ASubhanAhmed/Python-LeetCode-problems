'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

'''
# LEETCODE Problem # 20
# -Easy-

# class Solution(object):
#     def isValid(self, s):
        
#         """
#         :type s: str
#         :rtype: bool
#         """

class Solution(object):
    def isValid(s):
        dict = {"(":")", "[":"]", "{":"}"}

        #s = input("IsValid? : ")
        sp = list(s)
        i = 0
        try:
            while i<len(sp):
                if dict[sp[i]] == sp[i + 1]:
                    print(True)
                    i += 2
                else:
                    print(False)
                    break
        except IndexError:
            print(False)
    
s= "[}"
sss = Solution
sss.isValid(s="[}")

"""

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
    
"""