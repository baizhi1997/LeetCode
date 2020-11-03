
# @Title: 自除数 (Self Dividing Numbers)
# @Author: qinxinlei
# @Date: 2018-10-04 14:46:12
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans=[]
        for x in range(left,right+1):
            y=x
            while y:
                val=y%10
                if val==0 or x%(val):
                    break
                y//=10
            if not y:
                ans.append(x)
        return ans
