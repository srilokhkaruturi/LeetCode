class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate how many hours it takes Koko
        # to eat all bananas with speed k.
        def hours_needed(k):
            return sum(math.ceil(pile / k) for pile in piles)
        
        # Binary search
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) > h:
                left = mid + 1
            else:
                right = mid
                
        return left