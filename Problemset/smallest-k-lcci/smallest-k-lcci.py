
# @Title: 最小K个数 (Smallest K LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 16:49:58
# @Runtime: 128 ms
# @Memory: 21.7 MB

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, arr)
        
