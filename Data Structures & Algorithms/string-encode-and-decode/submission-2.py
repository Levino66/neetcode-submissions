class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            el = strs[i]
            length = int(len(el))
            key = str(length//100) + str(length//10%10) + str(length%10)
            s += key + el
        return s


    def decode(self, s: str) -> List[str]:
        i = 0
        out = []
        while i < len(s):
            key = int(s[i : i + 3]) + 1
            out.append(s[i + 3 : i + key + 2])
            i += key + 2
        return out