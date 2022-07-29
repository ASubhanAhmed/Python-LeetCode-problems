'''
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution(object):
    def addBinary(self, a, b):
        a_list = list(a)
        a_list.insert(0, "b")
        a_list.insert(0, "0")

        b_list = list(b)
        b_list.insert(0, "b")
        b_list.insert(0, "0")
        AA = ' '.join(a_list)
        BB = ' '.join(b_list)
        AA_join = "".join(AA.split())
        BB_join = "".join(BB.split())
        R = int(AA_join, 2)+int(BB_join, 2)
        R_bin = bin(R)
        new_R = R_bin.replace("0b", "")
        return new_R

# RunTime: 4ms ( a lot better than mine(16ms) )
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Initialize the result
        result = ''

        # Initialize the carry
        carry = 0

        # Traverse the string
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result

            # Compute the carry.
            carry = 0 if r < 2 else 1

        if carry != 0:
            result = '1' + result
        return result

#Memory Usage: 13.1K MB ( a lot better than mine(13.7K MB) )
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p1 = len(a) - 1
        p2 = len(b) - 1
        result = ""
        carry = 0
        while(p1 >= 0 and p2 >= 0):
            sum_char = eval(a[p1]) + eval(b[p2]) + carry
            carry = sum_char // 2 #floor division
            result += str(sum_char % 2)
            p1 += -1
            p2 += -1
        while p1 >= 0:
            sum_char = eval(a[p1]) + carry
            carry = sum_char // 2 #floor division
            result += str(sum_char % 2)
            p1 += -1
        
        while p2 >= 0:
            sum_char = eval(b[p2]) + carry
            carry = sum_char // 2 #floor division
            result += str(sum_char % 2)
            p2 += -1
        if carry > 0:
            result += str(carry)
            
        return result[::-1]
        
            
"""
 

Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""