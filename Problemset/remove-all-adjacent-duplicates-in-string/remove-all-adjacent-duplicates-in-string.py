
# @Title: 删除字符串中的所有相邻重复项 (Remove All Adjacent Duplicates In String)
# @Author: qinxinlei
# @Date: 2019-05-19 19:37:34
# @Runtime: 76 ms
# @Memory: N/A

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)
