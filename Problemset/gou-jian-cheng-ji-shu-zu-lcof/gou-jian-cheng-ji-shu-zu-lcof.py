
# @Title: 构建乘积数组 (构建乘积数组 LCOF)
# @Author: qinxinlei
# @Date: 2020-05-14 22:01:33
# @Runtime: 100 ms
# @Memory: 22.9 MB

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        tmp1 = [1]
        tmp2 = [1]
        for i in range(len(a)-1):
            tmp1.append(tmp1[-1]*a[i])
            tmp2.append(tmp2[-1]*a[-i-1])
        ans = []
        for i in range(len(a)):
            ans.append(tmp1[i]*tmp2[-i-1])
        return ans
