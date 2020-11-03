
# @Title: 用栈操作构建数组 (Build an Array With Stack Operations)
# @Author: qinxinlei
# @Date: 2020-08-02 11:24:10
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        j = 0
        for i in range(1, target[-1]+1):
            if i == target[j]:
                ans.append("Push")
                j += 1
            else:
                ans.extend(["Push", "Pop"])
        return ans
