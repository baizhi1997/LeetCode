
# @Title: 种花问题 (Can Place Flowers)
# @Author: qinxinlei
# @Date: 2018-11-04 22:01:15
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        k=1
        for i in flowerbed:
            if i:
                n-=(k-1)//2
                k=0
            else:
                k+=1
        return k//2-n>=0
