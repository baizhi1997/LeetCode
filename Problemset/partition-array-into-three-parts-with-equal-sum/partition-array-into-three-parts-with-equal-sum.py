
# @Title: 将数组分成和相等的三个部分 (Partition Array Into Three Parts With Equal Sum)
# @Author: qinxinlei
# @Date: 2019-03-29 19:41:08
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s=sum(A)
        if s%3!=0:
            return False
        t=sum(A)//3
        y=0
        k=0
        for x in A:
            y+=x
            if y==t:
                y=0
                k+=1
                if k==2:
                    return True
        return False
