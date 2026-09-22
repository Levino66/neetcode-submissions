class Solution:
    def isAnagram(self, s: List, t: list) -> bool:
        hashmap1 = dict()
        for l in s:
            hashmap1[l] = hashmap1.get(l, 0) + 1
        for l in t:
            hashmap1[l] = hashmap1.get(l, 0) - 1
        return not (any(i for i in hashmap1.values()))


