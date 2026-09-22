class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in t:
            hashmap[i] = hashmap.get(i, 0) - 1
        return False if any(hashmap.values()) else True