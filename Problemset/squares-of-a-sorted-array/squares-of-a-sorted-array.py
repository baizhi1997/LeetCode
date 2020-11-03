
# @Title: 有序数组的平方 (Squares of a Sorted Array)
# @Author: qinxinlei
# @Date: 2019-03-01 15:51:32
# @Runtime: 212 ms
# @Memory: N/A

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans=[]
        l,r=0,len(A)-1
        while l<=r:
            if abs(A[l])>abs(A[r]):
                ans.append(A[l]**2)
                l+=1
            else:
                ans.append(A[r]**2)
                r-=1
        return ans[::-1]
