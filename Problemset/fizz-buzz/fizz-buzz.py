
# @Title: Fizz Buzz (Fizz Buzz)
# @Author: qinxinlei
# @Date: 2018-10-19 21:48:05
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[str(i+1) for i in range(n)]
        if n>2:
            ans[2::3]=["Fizz"]*(n//3)
        if n>4:
            ans[4::5]=["Buzz"]*(n//5)
        if n>14:
            ans[14::15]=["FizzBuzz"]*(n//15)
        return ans
     return ans
