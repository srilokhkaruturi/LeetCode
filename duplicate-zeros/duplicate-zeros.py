class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        addedZero = False
        
        # go through the array
        for index in range(0, len(arr)):
            # when we find a zero .. insert 0 in plus index .. remove one from end
            try:
                if arr[index] == 0 and addedZero != True:
                    arr.insert(index+1, 0)
                    arr.pop(-1)
                    addedZero = True
                else:
                    addedZero = False
            except:
                pass
                
        