
# @Title: 用 Rand7() 实现 Rand10() (Implement Rand10() Using Rand7())
# @Author: qinxinlei
# @Date: 2018-11-28 17:09:59
# @Runtime: 548 ms
# @Memory: N/A

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x=rand7()+(rand7()-1)*7
        return x%10+1 if x<41 else self.rand10()
