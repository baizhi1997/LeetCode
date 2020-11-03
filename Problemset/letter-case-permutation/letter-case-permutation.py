
# @Title: 字母大小写全排列 (Letter Case Permutation)
# @Author: qinxinlei
# @Date: 2018-10-22 14:34:58
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S=S.lower()
        ans=[""]
        for i in S:
            tmp=[]
            for j in ans:
                tmp.append(j+i)
            if i.isalpha():
                for j in ans:
                    tmp.append(j+i.upper())
            ans=tmp
        return ans
