
# @Title: 仅仅反转字母 (Reverse Only Letters)
# @Author: qinxinlei
# @Date: 2018-10-22 11:47:54
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S=list(S)
        L=len(S)
        r=L-1
        l=0
        while l<r:
            while l<L and not S[l].isalpha():
                l+=1
            while r>-1 and not S[r].isalpha():
                r-=1
            if l<r:
                S[l],S[r]=S[r],S[l]
                l+=1
                r-=1
        return ''.join(S)
