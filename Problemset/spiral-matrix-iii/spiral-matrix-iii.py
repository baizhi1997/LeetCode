
# @Title: 螺旋矩阵 III (Spiral Matrix III)
# @Author: qinxinlei
# @Date: 2018-11-22 13:41:32
# @Runtime: 184 ms
# @Memory: N/A

class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        step=1
        ans=[[r0,c0]]
        while len(ans)<R*C:
            if 0<=r0<R:
                for _ in range(step):
                    c0+=1
                    if 0<=c0<C:
                        ans.append([r0,c0])
            else:
                c0+=step
            if 0<=c0<C:
                for _ in range(step):
                    r0+=1
                    if 0<=r0<R:
                        ans.append([r0,c0])
            else:
                r0+=step
            step+=1
            if 0<=r0<R:
                for _ in range(step):
                    c0-=1
                    if 0<=c0<C:
                        ans.append([r0,c0])
            else:
                c0-=step
            if 0<=c0<C:
                for _ in range(step):
                    r0-=1
                    if 0<=r0<R:
                        ans.append([r0,c0])
            else:
                r0-=step
            step+=1
        return ans
