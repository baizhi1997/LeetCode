
# @Title: 字母移位 (Shifting Letters)
# @Author: qinxinlei
# @Date: 2019-01-15 12:15:26
# @Runtime: 128 ms
# @Memory: N/A

class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        ans=[]
        tmp=sum(shifts)%26
        for i,c in enumerate(S):
            index=ord(c)-ord('a')
            ans.append(chr(ord('a')+(index+tmp)%26))
            tmp=(tmp-shifts[i])%26
        return ''.join(ans)
