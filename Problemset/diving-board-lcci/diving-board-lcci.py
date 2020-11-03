
# @Title: 跳水板 (Diving Board LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 10:20:38
# @Runtime: 64 ms
# @Memory: 17.3 MB

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter*k]
        return [i*longer+(k-i)*shorter for i in range(k+1)]
