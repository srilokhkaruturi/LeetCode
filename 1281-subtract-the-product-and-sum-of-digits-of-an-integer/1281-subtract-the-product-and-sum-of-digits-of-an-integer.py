class Solution:
    def separate(self, n):
        word = str(n)
        return word
    def productdigits(self, n):
        digitlist = self.separate(n)
        product = 1
        for digit in digitlist:
            product=product*int(digit)
        return product
    def sumdigits(self, n):
        digitlist = self.separate(n)
        sumdigits = 0
        for digit in digitlist:
            sumdigits=sumdigits+int(digit)
        return sumdigits
    def subtractProductAndSum(self, n: int) -> int:        
        return self.productdigits(n)-self.sumdigits(n)