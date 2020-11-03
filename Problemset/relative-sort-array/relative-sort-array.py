
# @Title: 数组的相对排序 (Relative Sort Array)
# @Author: qinxinlei
# @Date: 2019-08-08 15:55:34
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key = lambda x: (dic.get(x, 1001), x))
