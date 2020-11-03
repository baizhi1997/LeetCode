
# @Title: 分式化简 (Deep Dark Fraction)
# @Author: qinxinlei
# @Date: 2020-08-02 11:42:14
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        #结果模拟,一个记录分子，一个记录分母
        res = [cont[len(cont)-1],1]
        #迭代
        for i in range(len(cont)-2,-1,-1):
            tmp = res[1]
            res[1] = res[0]
            res[0] = cont[i] * res[1] + tmp
        return res

