
# @Title: 从英文中重建数字 (Reconstruct Original Digits from English)
# @Author: qinxinlei
# @Date: 2018-11-25 14:15:22
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic=collections.Counter(s)
        ans=""
        ans+="0"*dic['z']
        ans+="1"*(dic['o']-dic['z']-dic['w']-dic['u'])
        ans+="2"*dic['w']
        ans+="3"*(dic['h']-dic['g'])
        ans+="4"*dic['u']
        ans+="5"*(dic['f']-dic['u'])
        ans+="6"*dic['x']
        ans+="7"*(dic['s']-dic['x'])
        ans+="8"*dic['g']
        ans+="9"*(dic['i']-dic['x']-dic['g']-dic['f']+dic['u'])
        return ans
