class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        result: int = 0
        signs = {'/','*', '-', '+'}
        nums = []

        for val in tokens:
            if val in signs:
                if val == '/':
                    subres = nums[-2] / nums.pop()
                    if subres != subres//1 and subres < 0:
                        subres += 1
                    nums[-1] = subres//1

                if val == '*':
                    nums[-1] = nums[-2] * nums.pop()
                if val == '-':
                    nums[-1] = nums[-2] - nums.pop()
                if val == '+':
                    nums[-1] = nums[-2] + nums.pop()

            else:
                nums.append(int(val))

        result = int(nums[0])
        return result