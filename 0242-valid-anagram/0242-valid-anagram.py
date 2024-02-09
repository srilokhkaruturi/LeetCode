class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for element in s:
            t=t.replace(element, "", 1)
        
        if len(t) == 0:
            return True