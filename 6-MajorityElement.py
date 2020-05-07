"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

"""
#Solution
class Solution:
            
    def majorityElement(self, nums: List[int]) -> int:
        a=collections.Counter(nums)
        l=max(a.values())
        for key,value in a.items():
            if l == value :
                return key
            
                
                
