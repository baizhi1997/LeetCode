
# @Title: n 的第 k 个因子 (The kth Factor of n)
# @Author: qinxinlei
# @Date: 2020-07-29 16:05:48
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        factor = 1
        while factor * factor <= n:
            if n % factor == 0:
                count += 1
                if count == k:
                    return factor
            factor += 1
        factor -= 1
        if factor * factor == n:
            factor -= 1
        while factor > 0:
            if n % factor == 0:
                count += 1
                if count == k:
                    return n // factor
            factor -= 1
        return -1

