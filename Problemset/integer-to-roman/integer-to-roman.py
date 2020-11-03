
# @Title: 整数转罗马数字 (Integer to Roman)
# @Author: qinxinlei
# @Date: 2018-09-30 19:26:21
# @Runtime: 72 ms
# @Memory: N/A

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s1=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        s2=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        s3=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        s4=["","M","MM","MMM"]
        ans=s4[num//1000]+s3[num//100%10]+s2[num//10%10]+s1[num%10]
        return ans
    
