class Solution:
    def validPalindrome(self, s: str) -> bool:
        pointerOne = 0
        pointerTwo = len(s)-1
        
        while pointerOne <= pointerTwo:
            if s[pointerOne] != s[pointerTwo]:
                i_one = pointerOne
                j_one = pointerTwo - 1
                
                i_two = pointerOne + 1
                j_two = pointerTwo
                
                while(i_one < j_one and s[i_one] == s[j_one]):
                    i_one += 1
                    j_one -= 1
                
                if(i_one >= j_one):
                    return True
                
                while(i_two < j_two and s[i_two] == s[j_two]):
                    i_two += 1
                    j_two -= 1
                
                if(i_two >= j_two):
                    return True
                
                return False
            
            pointerOne += 1
            pointerTwo -= 1
        
        return True