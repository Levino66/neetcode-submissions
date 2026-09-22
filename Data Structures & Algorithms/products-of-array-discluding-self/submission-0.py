class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeros = 0
        prod = 1
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                zeros += 1
            else:
                prod *= n

        if zeros > 1:
            return [0] * len(nums)
        
        elif zeros == 1:
            for i in nums:
                if i:
                    res.append(0)
                else:
                    res.append(prod)
            return res
        
        else:
            for i in nums:
                res.append(prod // i)
            return res