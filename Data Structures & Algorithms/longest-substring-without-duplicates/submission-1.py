class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = dict()
        maxLen = 0
        l = r = 0
        for i, n in enumerate(s):
            if n in characters and l <= characters[n]:
                maxLen = max(maxLen, i - l)
                l = characters[n] + 1
            characters[n] = i
        maxLen = max(maxLen, len(s) - l)
        return maxLen

