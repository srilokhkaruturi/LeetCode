class Solution:
    def fib(self, n: int) -> int:
        mem_array = {}
        result = 0
        if n in mem_array:
            return mem_array[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            result = self.fib(n-1) + self.fib(n-2)
        
        mem_array[n] = result
        
        return result
        
        