
# @Title: 下一个更大元素 III (Next Greater Element III)
# @Author: qinxinlei
# @Date: 2018-12-10 15:39:23
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return -1
        n=list(str(n))[::-1]
        i=1
        while n[i]>=n[i-1]:
            i+=1
            if i==len(n):
                return -1
        j=bisect.bisect(n[:i],n[i])
        n[i],n[j]=n[j],n[i]
        n[:i]=reversed(n[:i])
        ans=int(''.join(n[::-1]))
        return ans if ans<pow(2,31) else -1
