'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

# RunTime: 12/30ms , Memory: 13.8/13.4 MB
class Solution:
    def lengthOfLastWord(self,s):
        S = s.strip()
        Mod = S.split(" ")
        print(len(Mod[-1]))
        return len(Mod[-1])

s = "Hello World"
x = Solution().lengthOfLastWord(s)

"""
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.


Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.


Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""