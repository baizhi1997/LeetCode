
# @Title: 根据数字二进制下 1 的数目排序 (Sort Integers by The Number of 1 Bits)
# @Author: qinxinlei
# @Date: 2020-07-31 16:09:34
# @Runtime: 60 ms
# @Memory: 13.5 MB

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
