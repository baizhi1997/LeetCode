
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: qinxinlei
# @Date: 2018-09-30 21:21:06
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans=list(dic[digits[0]])
        for c in digits[1:]:
            ans=[s1+s2 for s1 in ans for s2 in dic[c]]
        return ans
