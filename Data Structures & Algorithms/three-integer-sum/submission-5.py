class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: set[List[int]] = set()
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -num:
                    left += 1
                    continue
                if nums[left] + nums[right] > -num:
                    right -= 1
                    continue
                if nums[left] + nums[right] == -num:
                    result.add((nums[left], num, nums[right]))
                    left, right = left + 1, right - 1
        return [list(i) for i in result]
                
                
                