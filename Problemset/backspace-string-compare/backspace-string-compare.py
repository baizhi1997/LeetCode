
# @Title: 比较含退格的字符串 (Backspace String Compare)
# @Author: qinxinlei
# @Date: 2018-11-21 16:09:40
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i,j=len(S),len(T)
        backS=backT=0
        while True:
            i,j=i-1,j-1
            while i>=0 and (backS or S[i]=='#'):
                backS+=1 if S[i]=='#' else -1
                i-=1
            while j>=0 and (backT or T[j]=='#'):
                backT+=1 if T[j]=='#' else -1
                j-=1
            if i<0 or j<0:
                return i==j==-1
            if S[i]!=T[j]:
                return False
