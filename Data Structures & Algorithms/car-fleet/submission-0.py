class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 1

        posSpeed = [[position[i], speed[i]] for i in range(len(speed))]
        posSpeed.sort()

        prevTime = (target - posSpeed[-1][0]) / posSpeed[-1][1]

        for i in range(2, len(posSpeed) + 1):
            newTime = (target - posSpeed[-i][0]) / posSpeed[-i][1]

            if newTime <= prevTime:
                continue

            prevTime = newTime    
            ans += 1

        return ans
