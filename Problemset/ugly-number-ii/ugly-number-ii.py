
# @Title: 丑数 II (Ugly Number II)
# @Author: qinxinlei
# @Date: 2018-10-14 21:51:58
# @Runtime: 112 ms
# @Memory: N/A

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly=[1]
        i,j,k=0,0,0
        for _ in range(n-1):
            x,y,z=2*ugly[i],3*ugly[j],5*ugly[k]
            tmp=min(x,y,z)
            if x==tmp:
                i+=1
            if y==tmp:
                j+=1
            if z==tmp:
                k+=1
            ugly.append(tmp)
        return ugly[-1]
