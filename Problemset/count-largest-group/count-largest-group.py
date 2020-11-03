
# @Title: 统计最大组的数目 (Count Largest Group)
# @Author: qinxinlei
# @Date: 2020-08-02 11:13:08
# @Runtime: 56 ms
# @Memory: 13.2 MB

class Solution:
    def countLargestGroup(self, n: int) -> int:
        f = [0] * (n + 1)
        c = [0] * 37
        for i in range(1, n+1):
            f[i] = f[i // 10] + i % 10
            c[f[i]] += 1
        maxc = max(c)
        return sum([i == maxc for i in c])
