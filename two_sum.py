'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num 

            if need in seen:
                return [seen[need], i]
            
            seen[num] = i

        return "not found"
    
nums = [2, 11, 7, 14]
target = 18

print(twoSum(nums, target))

'''
we track each number and index in our list, in each iteration we check if the needed number is in seen,
if not we store the current number in it, if we see it, we return the seen number's index and the current number index as a list

'''
