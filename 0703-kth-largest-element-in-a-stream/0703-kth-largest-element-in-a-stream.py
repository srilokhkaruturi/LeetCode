class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        # APPEND NEW VALUE TO NUMS
        self.nums.append(val)
        
        # DEFINE NUMS COPY
        self.nums.sort()
        
        return self.nums[-1 * self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)