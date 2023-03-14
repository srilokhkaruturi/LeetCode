class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        # first pass (get products)
        prefix = [0] * len(nums)
        product = 1
        for i in range(0, len(nums)):
            prefix[i] = product * nums[i]
            product = prefix[i]
        # second pass (get products starting from tail to beginning)
        postfix = [0] * len(nums)
        product = 1 
        for j in range(len(nums)-1, -1, -1):
            postfix[j] = product * nums[j]  
            product = postfix[j]
            
        print(prefix)
        print(postfix)

            
        # find output array 
        outputArray = [0] * len(nums)
        for i in range(0, len(nums)):
            # get pre (product)
            pre = 0
            if i > 0:
                pre = prefix[i-1]
            else:
                pre = 1
                
            # get postfix
            post = 0
            if i < len(nums)-1:
                post = postfix[i+1]
            else:
                post = 1 
                
            # set 
            outputArray[i] = pre*post
            
        return outputArray
        
                    