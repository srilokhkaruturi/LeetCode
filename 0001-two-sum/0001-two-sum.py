class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # DEFINE HASHMAP via dictionary
        hashMap = []
        
        for i in range(0, len(nums)):
            lookingFor = target - nums[i] 
            if lookingFor in hashMap:
                return [hashMap.index(lookingFor), i]
            else:
                hashMap.append(nums[i])
            
        return []