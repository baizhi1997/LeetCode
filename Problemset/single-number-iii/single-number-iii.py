
# @Title: 只出现一次的数字 III (Single Number III)
# @Author: qinxinlei
# @Date: 2018-10-29 18:45:23
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor=0
        ans1=0
        ans2=0
        for num in nums:
            xor^=num
        tmp=1
        while tmp&xor==0:
            tmp=tmp<<1
        for num in nums:
            if num&tmp:
                ans1^=num
            else:
                ans2^=num
        return [ans1,ans2]
