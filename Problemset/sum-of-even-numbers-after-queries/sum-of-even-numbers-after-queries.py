
# @Title: 查询后的偶数和 (Sum of Even Numbers After Queries)
# @Author: qinxinlei
# @Date: 2019-03-01 15:04:54
# @Runtime: 180 ms
# @Memory: N/A

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        tmp=sum([x for x in A if x&1==0])
        ans=[]
        for v,i in queries:
            if A[i]&1==0:
                tmp-=A[i]
            A[i]+=v
            if A[i]&1==0:
                tmp+=A[i]
            ans.append(tmp)
        return ans
