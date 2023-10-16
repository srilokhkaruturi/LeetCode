class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the original color of the starting pixel
        originalColor = image[sr][sc]
        
        # If the starting color is already the target color, return the image as is
        if originalColor == color:
            return image

        # DFS function to flood fill
        def dfs(i, j):
            # If the pixel is out of the image boundaries or not of the original color, return
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != originalColor:
                return
        
            # Change the color of the pixel
            image[i][j] = color
        
            # Recur for all its 4-directionally connected neighbors
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Start the flood fill from the starting pixel
        dfs(sr, sc)
    
        return image