"""
You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for 
one element which appears exactly once. Find this single element that appears only once.

"""

#Solution

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a=collections.Counter(nums)
        listOfItems = a.items()
        for item  in listOfItems:
            if item[1] == 1:
                return(item[0])