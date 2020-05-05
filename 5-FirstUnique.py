"""
Given a string, find the first non-repeating character in it and return it's index.

If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""

#Solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=collections.Counter(s)
        for i in range(len(s)):
            if a[s[i]]==1:
                return i
                break
            else:
                pass
        return -1
        