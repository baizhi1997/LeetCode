
# @Title: 将整数按权重排序 (Sort Integers by The Power Value)
# @Author: qinxinlei
# @Date: 2020-06-17 10:21:24
# @Runtime: 196 ms
# @Memory: 26.8 MB

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        f = {1: 0}
        def getF(x):
            if x in f:
                return f[x]
            f[x] = (getF(x * 3 + 1) if x % 2 == 1 else getF(x // 2)) + 1
            return f[x]
        v = list(range(lo, hi + 1))
        v.sort(key=lambda x: (getF(x), x))
        return v[k - 1]

