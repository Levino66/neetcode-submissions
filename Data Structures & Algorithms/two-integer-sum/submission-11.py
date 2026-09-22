class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsset = dict()
        for i, num in enumerate(nums):
            if num in numsset:
                return [numsset[num], i]
            else:
                numsset[target - num] = i
            
