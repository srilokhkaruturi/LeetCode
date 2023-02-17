class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # implement binary search on nums with target
        p1 = 0
        p2 = len(nums)-1
        target_index = 0

        while (p1 <= p2):
            middle = (p2+p1) // 2
            if nums[middle] > target:
                p2 = middle - 1

            elif nums[middle] < target:
                p1 = middle + 1

            else:
                return middle

        target_index = p1

        return target_index

            
    