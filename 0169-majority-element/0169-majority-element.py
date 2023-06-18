class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        hash_map = dict()
        majority_element = -1
        for element in nums:
            if element in hash_map:
                hash_map[element] += 1
                if hash_map[element] >= (len(nums)/2):
                    majority_element = element
            else:
                hash_map[element] = 1

        return majority_element