
# @Title: 找到 K 个最接近的元素 (Find K Closest Elements)
# @Author: qinxinlei
# @Date: 2019-01-15 10:39:26
# @Runtime: 188 ms
# @Memory: N/A

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i=bisect.bisect_left(arr,x)
        l=max(0,i-k)
        r=min(len(arr)-1,i+k-1)
        while r-l>k-1:
            if x-arr[l]<=arr[r]-x:
                r-=1
            else:
                l+=1
        return arr[l:r+1]
