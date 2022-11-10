class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # DEFINE RETURN ARRAY
        returnArr = []
        
        # DEFINE DICTIONARY
        dictionary = {}
        
        for element in nums:
            if element in dictionary:
                dictionary[element] += 1
            else:
                dictionary[element] = 1
                
        while(k > 0 ):
            # DEFINE HIGHEST FREQ
            highestFrequency = 0
            
            # FIND THE HIGHEST FREQ
            for element in dictionary:
                if dictionary[element] > highestFrequency:
                    highestFrequency = dictionary[element]
                    highestFrequencyElement = element
            
            # APPEND TO RETURNARRAY
            returnArr.append(highestFrequencyElement)
            
            # DELETE THE HIGHEST FREQ FROM DICTIONARY 
            dictionary.pop(highestFrequencyElement)
            
            # REDUCE K by 1
            k -= 1
        
        return returnArr