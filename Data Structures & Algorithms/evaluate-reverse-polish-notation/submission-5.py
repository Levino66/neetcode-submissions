class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack: list[int] = []
        for val in tokens:

            if val == '/':
                num_1, num_2 = stack.pop(), stack.pop()
                stack.append(int(num_2 / num_1))
            elif val == '-':
                num_1, num_2 = stack.pop(), stack.pop()
                stack.append(num_2 - num_1)

            elif val == '*':
                stack.append(stack.pop() * stack.pop())
            elif val == '+':
                stack.append(stack.pop() + stack.pop())

            else:
                stack.append(int(val))

        return stack[0]
