class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        
        for element in nums:
            if element in hashmap:
                return True
            else:
                hashmap.add(element)
                
                
        return False

        
        