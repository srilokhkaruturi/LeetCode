class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_substrings = []
        existent_chars = set()
        substring = ''
        
        
        # to add to unique substrings 
            # when the same character appears
            # at the ending 
        for i in range(0, len(s)):
            existent_chars = set()
            substring = ''
            for k in range(i, len(s)):
                if s[k] in existent_chars:
                    unique_substrings.append(substring)
                    break
                else:
                    substring += s[k]
                    existent_chars.add(s[k])
                    
                    if (k+1) == len(s):
                        unique_substrings.append(substring)


                   
        # find largest unique substrings
        largest_length_substring = 0
        
        for element in unique_substrings:
            if len(element) > largest_length_substring:
                largest_length_substring = len(element)
        
        
        return largest_length_substring
                
                
        