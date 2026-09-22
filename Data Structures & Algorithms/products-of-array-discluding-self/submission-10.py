class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1 for i in range(length)]
        pref = nums[0]
        post = nums[-1]
        for i in range(1, length):
            res[i] *= pref
            pref *= nums[i]
            res[-i - 1] *= post
            post *= nums[-i - 1]

        return res
