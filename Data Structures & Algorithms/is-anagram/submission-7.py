class Solution:
    def isAnagram(self, s: List, t: list) -> bool:
        return Counter(s) == Counter(t)


