
# @Title: 一次编辑 (One Away LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 15:46:41
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if not first:
            return len(second) <= 1
        if not second:
            return len(first) <= 1
        if first[0] == second[0]:
            return self.oneEditAway(first[1:], second[1:])
        return first[1:] == second[1:] or first[1:] == second or first == second[1:]
