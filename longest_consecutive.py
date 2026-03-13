'''
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

from typing import List

def longestConsecutive(nums: List[int]) -> int:

    nums_set = set(nums)
    max_length = 0
    best_sequence = []

    for n in nums_set:
        if n - 1 not in nums_set:
            length = 1
            sequence = [n]

            while n + length in nums_set:
                sequence.append(n + length)
                length += 1

            if length > max_length:
                max_length = length
                best_sequence = sequence

    print(f"best sequence: {best_sequence}, length: {max_length}")

    return max_length




nums = [100,4,200,1,3,2]
longestConsecutive(nums)