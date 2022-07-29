'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''

# class Solution:
#     def singleNumber(self, nums):
#         r = []
#         if len(nums)==1:
#             for i in nums:
#                 gama = 1
#         else:
#             for i in nums:
#                 if i not in r:
#                     r.append(i)
#             for elem in r:
#                 nums.remove(elem)
#             #r.remove(nums[0])
#                 r.remove(nums[0])
#             #while
#                 for i in r:
#                     gama = i

#         return gama

class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor



#RunTime: 94ms ( Mine(150ms) )
from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cur_single = 0
        for num in nums:
            cur_single ^= num
        
        return cur_single
        


# Memory Usage: 14.7 MB (Mine(15.4 MB) )
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #single = []
        for i in nums:
            if nums.count(i)==1:
                return i
                #single.append(i)
        #return single



"""
Example 1:

Input: nums = [2,2,1]
Output: 1


Example 2:

Input: nums = [4,1,2,1,2]
Output: 4


Example 3:

Input: nums = [1]
Output: 1
 


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""
