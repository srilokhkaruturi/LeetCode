class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # DEFINE OUR DICTIONARY
        groupAnagram = defaultdict(list)
        
        # GO THROUGH EVERY ELEMENT 
        for elementStr in strs:
            countChars = [0] * 26
            for char in elementStr:
                # CHECK IF THE UNICODE REPRESENTATION IS GOING TO BE THE 
                countChars[ord(char) - ord("a")] += 1
            
            groupAnagram[tuple(countChars)].append(elementStr)
            
        return groupAnagram.values()
    
        # m * n
        # m = number of strings
        # n = average length of each string