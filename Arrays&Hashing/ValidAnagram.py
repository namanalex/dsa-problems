class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        base = ord('a')

        for ch in s:
            count[ord(ch) - base] += 1
        for ch in t:
            count[ord(ch) - base] -= 1
        
        for v in count:
            if v != 0:
                return False
        return True