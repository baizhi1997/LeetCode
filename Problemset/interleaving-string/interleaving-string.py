
# @Title: 交错字符串 (Interleaving String)
# @Author: qinxinlei
# @Date: 2019-05-07 10:48:27
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        last = set([(0, 0)])
        for char in s3:
            current = set()
            for i, j in last:
                if i < l1 and s1[i] == char:
                    current.add((i + 1, j))
                if j < l2 and s2[j] == char:
                    current.add((i, j + 1))
            if not current:
                return False
            last = current
        return True
