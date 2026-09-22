class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        answer = 0
        while l <= r:
            areaR = min(heights[l], heights[r]) * (r - l)
            answer = max(answer, areaR)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return answer