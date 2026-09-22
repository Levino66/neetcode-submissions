class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setN = dict()
        for i in range(len(nums)):
            if target - nums[i] in setN:
                return [setN[target - nums[i]], i]
            else:
                setN[nums[i]] = i