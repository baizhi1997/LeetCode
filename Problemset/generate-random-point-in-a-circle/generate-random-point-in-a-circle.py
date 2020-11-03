
# @Title: 在圆内随机生成点 (Generate Random Point in a Circle)
# @Author: qinxinlei
# @Date: 2019-09-11 15:51:52
# @Runtime: 164 ms
# @Memory: N/A

import random
class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            if (x - self.x_center)**2 + (y - self.y_center)**2 <= self.radius**2:
                return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
