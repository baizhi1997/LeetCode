
# @Title: 数组形式的整数加法 (Add to Array-Form of Integer)
# @Author: qinxinlei
# @Date: 2019-03-01 14:46:57
# @Runtime: 168 ms
# @Memory: N/A

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i=0
        while K and i<len(A):
            i+=1
            K,A[-i]=divmod(A[-i]+K,10)
        return [int(x) for x in list(str(K))]+A if K else A
