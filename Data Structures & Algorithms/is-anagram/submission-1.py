class Solution:
    def Counter(dictionary):
        dictionary_Counter = dict()
        for i in dictionary:
            if i in dictionary_Counter:
                dictionary_Counter[i] += 1
            else:
                dictionary_Counter[i] = 1
        return dictionary_Counter




    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return Counter(s) == Counter(t)
        return False