class Solution:
    def maxArea(self, height: List[int]) -> int:     
        
        maxVolume = 0
        i = 0
        j = len(height)-1
        
        while(i<j):
            minimum = min(height[i], height[j])
            volume = (j-i)*minimum

            if volume > maxVolume:
                maxVolume = volume
                
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
                
                    
                
        return maxVolume
        