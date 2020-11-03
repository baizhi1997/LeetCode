
# @Title: 1比特与2比特字符 (1-bit and 2-bit Characters)
# @Author: qinxinlei
# @Date: 2018-11-17 14:20:29
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        l=len(bits)-1
        i=0
        while i<l:
            if bits[i]:
                i+=2
            else:
                i+=1
        return i==l
