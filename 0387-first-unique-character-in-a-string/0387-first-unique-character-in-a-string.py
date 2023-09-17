class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        
        # create an occurrences dict
        # key = item
        # value = count
        for i in range(0, len(s)):
            if s[i] in char_dict:
                char_dict[s[i]] += 1
            else:
                char_dict[s[i]] = 1
        
        # find the first one that is 1
        for value in char_dict:
            if char_dict[value] == 1:
                return s.find(value)
            
        return -1
                
        