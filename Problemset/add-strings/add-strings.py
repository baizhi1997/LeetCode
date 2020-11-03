
# @Title: 字符串相加 (Add Strings)
# @Author: qinxinlei
# @Date: 2018-11-07 12:14:46
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=num1[::-1]
        num2=num2[::-1]
        l=max(len(num1),len(num2))
        if len(num1)>len(num2):
            num2+='0'*(l-len(num2))
        else:
            num1+='0'*(l-len(num1))
        carry=0
        ans=''
        for i in range(l):
            carry=carry+int(num1[i])+int(num2[i])
            ans+=str(carry%10)
            carry//=10
        if carry:
            ans+='1'
        return ans[::-1]
