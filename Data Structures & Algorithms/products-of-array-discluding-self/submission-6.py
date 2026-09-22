class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1 for i in range(length)]
        subprod = dict()
        subprod[0] = subprod[-1] = 1

        for i in range(1, length):
            subprod[i] = subprod[i - 1] * nums[i - 1]
            subprod[-i - 1] = subprod[-i] * nums[-i]
            print()

        for i in range(length):
            res[i] *= subprod[i]
            res[-length + i] *= subprod[-length + i]

        return res
