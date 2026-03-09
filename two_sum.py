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