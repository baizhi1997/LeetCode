
# @Title: 找出数组中的幸运数 (Find Lucky Integer in an Array)
# @Author: qinxinlei
# @Date: 2020-07-31 16:13:10
# @Runtime: 76 ms
# @Memory: 13.2 MB

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = collections.Counter(arr)
        ans = -1
        for k in dic:
            if dic[k] == k and k > ans:
                ans = k
        return ans
