
# @Title: 绘制直线 (Draw Line LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 17:19:19
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        anw=[0]*length
        wid=w//32
        n1,m1=divmod(x1,32)
        n2,m2=divmod(x2,32)
        for i in range(wid*y+n1,wid*y+n2+1):
            anw[i]=-1
        if m1!=0:anw[wid*y+n1]+=1<<(32-m1)
        anw[wid*y+n2]-=(1<<(32-m2-1))-1
        return anw

