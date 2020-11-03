
# @Title: 翻转图像 (Flipping an Image)
# @Author: qinxinlei
# @Date: 2018-10-18 19:00:33
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[i^1 for i in row][::-1] for row in A]
