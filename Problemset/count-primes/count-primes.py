
# @Title: 计数质数 (Count Primes)
# @Author: qinxinlei
# @Date: 2018-11-16 10:33:08
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        primes=[1]*n
        primes[0]=primes[1]=0
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i]=[0]*((n-1)//i-i+1)
        return sum(primes)
