
# @Title: 子数组异或查询 (XOR Queries of a Subarray)
# @Author: qinxinlei
# @Date: 2020-06-23 22:47:14
# @Runtime: 500 ms
# @Memory: 27.8 MB

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for num in arr:
            pre.append(pre[-1] ^ num)
        ans = list()
        for x, y in queries:
            ans.append(pre[x] ^ pre[y + 1])
        return ans

