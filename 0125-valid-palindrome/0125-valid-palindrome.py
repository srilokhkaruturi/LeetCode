class Solution:
    def isPalindrome(self, s: str) -> bool:
        # DEFINE TWO POINTERS
        beg = 0
        end = len(s) - 1
        
        s = s.lower()
        
        while(beg < end):
            if (not s[beg].isalnum()):
                beg = beg + 1 
                pass
            elif (not s[end].isalnum()):
                end = end - 1
                pass
            elif s[end].lower() != s[beg].lower():
                return False
            else:
                beg += 1
                end -= 1
                
        return True
        
                