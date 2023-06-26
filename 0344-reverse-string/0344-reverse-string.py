class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointerOne = 0
        pointerTwo = len(s)-1
        placeholder = None
        
        while pointerOne < pointerTwo:
            placeholder = s[pointerOne]
            s[pointerOne] = s[pointerTwo]
            s[pointerTwo] = placeholder
            
            pointerOne += 1
            pointerTwo -= 1