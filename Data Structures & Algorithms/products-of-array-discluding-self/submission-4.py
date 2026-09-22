class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
        subprod = dict()
        subprod[0] = subprod[-1] = 1

        for i in range(1, len(nums)):
            subprod[i] = subprod[i - 1] * nums[i - 1]
            subprod[-i - 1] = subprod[-i] * nums[-i]
            print()

        for i in range(len(nums)):
            res[i] *= subprod[i]
            res[-i - 1] *= subprod[-i - 1]

        return res
