class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = {}
        
        for i, character in enumerate(s):
            
            if character in letters:
                return character
            
            letters[character] = character