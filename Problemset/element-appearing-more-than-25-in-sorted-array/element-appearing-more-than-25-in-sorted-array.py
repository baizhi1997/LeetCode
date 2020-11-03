
# @Title: 有序数组中出现次数超过25%的元素 (Element Appearing More Than 25% In Sorted Array)
# @Author: qinxinlei
# @Date: 2020-08-02 15:07:35
# @Runtime: 132 ms
# @Memory: 14.6 MB

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        span = n // 4 + 1
        for i in range(0, n, span):
            iter_l = bisect.bisect_left(arr, arr[i])
            iter_r = bisect.bisect_right(arr, arr[i])
            if iter_r - iter_l >= span:
                return arr[i]
        return -1

