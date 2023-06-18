class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define hashset
        hash_set = []
        
        for i in range(0, len(nums)):
            lookingFor = target - nums[i] 
            if lookingFor in hashMap:
                return [hash_set.index(lookingFor), i]
            else:
                hash_set.append(nums[i])
            
        return []
