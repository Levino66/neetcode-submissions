class Solution:
    def isValid(self, s: str) -> bool:
        opening = {')':'(', '}':'{', ']':'['}
        order = []
        for i in s:
            if i in opening.values():
                order.append(i)
            elif order and order[-1] == opening[i]:
                order.pop()
            else:
                return False
        return not order


            