
# @Title: 机器人的运动范围 (机器人的运动范围  LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 15:14:42
# @Runtime: 60 ms
# @Memory: 13.6 MB

def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)

