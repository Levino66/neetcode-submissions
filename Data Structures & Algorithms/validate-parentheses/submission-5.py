class Solution:
    def isValid(self, s: str) -> bool:
        opening = {')':'(', '}':'{', ']':'['}
        order = []
        for i in s:
            if i in opening:
                
                if order and order[-1] == opening[i]:
                    order.pop()
                else:
                    return False
            else:
                order.append(i)
        return not order


            