class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Occurence Dictionary
        occurence_dict = OrderedDict()
        
        # O(n) - populate occurence dictionary
        for i in range(0, len(s)):
            if s[i] in occurence_dict:
                occurence_dict[s[i]] += 1
            else:
                occurence_dict[s[i]] = 1
            
        # Determine first unique character in string
        first_unique_char = ''
        first_unique_index = -1
        

        
        for key, value in occurence_dict.items():
            if value == 1:
                first_unique_char = key
                break
                
                
        # Determine index of the first char
        if first_unique_char == '':
            return first_unique_index
        else:
            for i in range(len(s)):
                if s[i] == first_unique_char:
                    return i
                
            
        
        
            