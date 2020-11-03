
# @Title: 构造矩形 (Construct the Rectangle)
# @Author: qinxinlei
# @Date: 2018-11-18 22:06:42
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in range(int(math.sqrt(area)),0,-1):
            if area%i==0:
                return [area//i,i]
