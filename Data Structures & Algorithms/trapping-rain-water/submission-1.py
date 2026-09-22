class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        highestL, highestR = height[l], height[r]

        while l < r:
            lowerof2highest = min(highestL, highestR)

            if highestL <= highestR:
                nexthigh = height[l + 1]
                
                if nexthigh >= highestL:
                    highestL = nexthigh
                else:
                    area += highestL - nexthigh
                l += 1

            else:    #height[l] > height[r]
                prevhigh = height[r - 1]

                if prevhigh >= highestR:
                    highestR = prevhigh
                else:
                    area += highestR - prevhigh
                r -= 1
        return area

            
