class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedSquares = [0] * len(nums)
        
        p1 = 0
        p2 = len(nums)-1
        indexToAdd = p2
        
        while p1<=p2:
            # compare which value in the pointer is bigger and then add
            if abs(nums[p1]) > nums[p2]:
                sortedSquares[indexToAdd] = nums[p1]**2
                indexToAdd -= 1
                p1 += 1
            else:
                sortedSquares[indexToAdd] = nums[p2]**2
                indexToAdd -= 1
                p2 -= 1
        
        return sortedSquares