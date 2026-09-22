class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
                 '1', '2', '3', '4', '5', '6', '7', '8', '9'}

        while left < right:
            while (s[left] not in chars) and left < right:
                left += 1

            while (s[right] not in chars) and left < right:
                right -= 1
        
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
                
        return True