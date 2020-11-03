
# @Title: 部分排序 (Sub Sort LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 14:12:06
# @Runtime: 108 ms
# @Memory: 30.5 MB

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        first, last = -1, -1
        tmpmax, tmpmin = float('-inf'), float('inf')
        for i in range(len(array)):
            if array[i] < tmpmax:
                last = i
            else:
                tmpmax = array[i]
        for i in range(len(array)-1, -1, -1):
            if array[i] > tmpmin:
                first = i
            else:
                tmpmin = array[i]
        return [first, last]
