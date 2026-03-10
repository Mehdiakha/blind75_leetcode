'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array. 
'''

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        l = len(nums)
        expected_array = [i for i in range(l+1)]

        for x in expected_array:
             if x not in nums: 
                return x

