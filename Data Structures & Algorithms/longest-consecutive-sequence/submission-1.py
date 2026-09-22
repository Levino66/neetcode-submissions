class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for n in nums:
            if not ((n - 1) in hashset):
                streak, curr = 1, n
                while (curr + 1) in hashset:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res





            


            