
# @Title: 判定字符是否唯一 (Is Unique LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 11:11:03
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if (mark & (1 << move_bit)) != 0:
                return False
            else:
                mark |= (1 << move_bit)
        return True

