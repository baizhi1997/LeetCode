
# @Title: 超级丑数 (Super Ugly Number)
# @Author: qinxinlei
# @Date: 2018-11-24 20:47:54
# @Runtime: 364 ms
# @Memory: N/A

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly=[1]
        l=len(primes)
        cnt=[0]*l
        tmp=[1]*l
        x=1
        for _ in range(n-1):
            for i in range(l):
                if x==tmp[i]:
                    tmp[i]=primes[i]*ugly[cnt[i]]
                    cnt[i]+=1
            x=min(tmp)
            ugly.append(x)
        return ugly[-1]
