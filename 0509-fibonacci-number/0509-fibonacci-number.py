class Solution:
    def fib(self, n: int) -> int:
        mem_array = {0: 0, 1: 1}
        result = 0
        
        if n in mem_array:
            return mem_array[n]
        else:
            mem_array[n] = self.fib(n-1) + self.fib(n-2)
        
        return mem_array[n]
        
        