
# @Title: 山羊拉丁文 (Goat Latin)
# @Author: qinxinlei
# @Date: 2018-11-17 14:03:09
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        S=S.split()
        for i in range(len(S)):
            if S[i][0] not in "aeiouAEIOU":
                S[i]=S[i][1:]+S[i][0]
            S[i]+="maa"+'a'*i
        return ' '.join(S)
