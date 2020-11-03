
# @Title: 重复至少 K 次且长度为 M 的模式 (Detect Pattern of Length M Repeated K or More Times)
# @Author: qinxinlei
# @Date: 2020-10-28 22:49:30
# @Runtime: 32 ms
# @Memory: 13.6 MB

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for l in range(n - m * k + 1):
            offset = 0
            while offset < m * k:
                if arr[l + offset] != arr[l + offset % m]:
                    break
                offset += 1
            if offset == m * k:
                return True
        return False

