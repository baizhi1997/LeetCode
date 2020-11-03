
# @Title: 和为零的N个唯一整数 (Find N Unique Integers Sum up to Zero)
# @Author: qinxinlei
# @Date: 2020-07-28 16:30:47
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [x for x in range(n - 1)]
        ans.append(-sum(ans))
        return ans

