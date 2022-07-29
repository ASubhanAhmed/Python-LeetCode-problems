'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
# My Soluion/Code/Logic.

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

# RunTime 46ms ( a lot better than mine(2889ms) ) 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        diff_map = {}
        array_size = len(nums)
        
        for i in range(array_size):
            if not nums[i] in diff_map:
                diff_map.update({(target-nums[i]):i})
            else:
                return [i,diff_map.get(nums[i])]
        
# Memory Usage: 13.6k MB ( Mine is 14.4K MB )

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if curr+nums[j]==target:
                    return [i, j]
        

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""