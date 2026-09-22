class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        minElemIndex = [nums[0], 0]
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                minElemIndex = min(minElemIndex, [nums[l], l])
                break
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
            minElemIndex = min(minElemIndex, [nums[m], m])
        print(minElemIndex)

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2 
            modernM = (m + minElemIndex[1]) % len(nums)
            print(m)
            if nums[modernM] < target:
                l = m + 1
            elif nums[modernM] > target:
                r = m - 1
            else:
                return modernM
        return -1
        return 'I am stupid'
        


        