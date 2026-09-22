class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0

        posSpeed = dict()
        for i in range(len(speed)):
            posSpeed[position[i]] = speed[i]

        prevTime = 0

        for i in range(target - 1, -1, -1):
            if type(posSpeed.get(i, False)) == int:
                newTime = (target - i) / posSpeed[i]

                if newTime <= prevTime:
                    continue

                prevTime = newTime    
                ans += 1

        return ans
