class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for i in range(len(temperatures))] 
        for i in range(2, len(temperatures) + 1):
            dif = 1
            while temperatures[-i] >= temperatures[-i + dif]:

                if ans[-i + dif] == 0:
                    dif = 0
                    break
                dif += ans[-i + dif]

            ans[-i] = dif
        return ans