class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # DEFINE START
        start = 0
        
        # DEFINE END 
        end = len(nums)-1
        
        # DEFINE MIDDLE ()
        
        # DEFINE WHILE LOOP
        while start <= end:
            mid = start + (end - start) // 2;
            # WHEN THE TARGET IS LESS THAN THE MIDDLE I WANT TO MOVE THE END TO THE MIDDLE
            # RECALCULATE MIDDLE
            if target < nums[mid]:
                end = mid - 1
            if target > nums[mid]:
                start = mid + 1
            if target == nums[mid]:
                return mid
                
        # RETURN 
        return -1