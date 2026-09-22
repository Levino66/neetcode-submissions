class Solution:
    def isAnagram(self, s: List, t: list) -> bool:
        hashmap1 = dict()
        hashmap2 = dict()
        for l in s:
            hashmap1[l] = hashmap1.get(l, 0) + 1
        for l in t:
            hashmap2[l] = hashmap2.get(l, 0) + 1
        if hashmap1 == hashmap2:
            return True
        return False


