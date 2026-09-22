class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        answer = min(heights[l], heights[r]) * (r - l)
          
        while l <= r:
            if heights[l] <= heights[r]:
                m = l + 1
                while m < r and heights[l] >= heights[m]:
                    m += 1
                
                if m < r:
                    areaR = min(heights[m], heights[r]) * (r - m)
                    answer = max(answer, areaR)
                l = m
            else:
                m = r - 1
                while l < m and heights[r] >= heights[m]:
                    m -= 1
                
                if l < m:
                    areaL = min(heights[l], heights[m]) * (m - l)
                    answer = max(answer, areaL)
                r = m
        return answer