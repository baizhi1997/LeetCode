
# @Title: 交换和 (Sum Swap LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 21:44:55
# @Runtime: 52 ms
# @Memory: 19.3 MB

class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        dx = sum(array1) - sum(array2)
        if dx & 1:
            return []
        dx //= 2
        set1 = set([num-dx for num in array1])
        for num in array2:
            if num in set1:
                return [num+dx, num]
        return []
