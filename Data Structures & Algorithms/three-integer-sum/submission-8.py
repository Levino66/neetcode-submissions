class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force try
        res = list()
        length = len(nums)
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        print(i,j,k)
                        if not(([nums[i],nums[j],nums[k]] in res) or ([nums[i],nums[k],nums[j]] in res)
                            or ([nums[j],nums[k],nums[i]] in res) or ([nums[j],nums[i],nums[k]] in res)
                            or ([nums[k],nums[j],nums[i]] in res) or ([nums[k],nums[i],nums[j]] in res)):
                            res.append([nums[i],nums[j],nums[k]])
        return res                      

                
                