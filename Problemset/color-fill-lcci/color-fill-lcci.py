
# @Title: 颜色填充 (Color Fill LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 16:53:31
# @Runtime: 52 ms
# @Memory: 13.7 MB

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def draw(sr, sc):
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == oldColor and image[sr][sc] != newColor:
                image[sr][sc] = newColor
                draw(sr+1, sc)
                draw(sr-1, sc)
                draw(sr, sc+1)
                draw(sr, sc-1)
        oldColor = image[sr][sc]
        draw(sr, sc)
        return image
