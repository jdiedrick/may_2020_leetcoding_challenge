class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:   
        if image[sr][sc] == newColor:
            return image
        else:
            oldColor = image[sr][sc]
            self.floodFillHelper(image, sr, sc, newColor, oldColor)
        return image
            
    def floodFillHelper(self, image: List[List[int]], sr: int, sc: int, newColor: int, oldColor: int) -> List[List[int]]:   
            if sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0]) and image[sr][sc] == oldColor:
                image[sr][sc] = newColor
                self.floodFillHelper(image, sr + 1, sc, newColor, oldColor)
                self.floodFillHelper(image, sr - 1, sc, newColor, oldColor)
                self.floodFillHelper(image, sr, sc + 1, newColor, oldColor)
                self.floodFillHelper(image, sr, sc - 1, newColor, oldColor)
