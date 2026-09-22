class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setN = set()
        for i in range(len(nums)):
            if nums[i] in setN:
                return [nums.index(target - nums[i]), i]
            else:
                setN.add(target - nums[i])