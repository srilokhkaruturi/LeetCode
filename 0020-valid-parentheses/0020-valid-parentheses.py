class Solution:
    def isValid(self, s: str) -> bool:
        # DEFINE OUR STACK
        stack = []
        
        # DEFINE OUR HASHMAP
        closeToOpen = {
            ")":"(",
            "}":"{",
            "]":"["
        }
    
        # GO THROUGH ALL ELEMENTS
        for character in s:
            # CHECK TO SEE IF IT AS CLOSING ONE
            if character in closeToOpen:
                if stack and stack[-1] == closeToOpen[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
                    
        if stack:
            return False
        else:
            return True