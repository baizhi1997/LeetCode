
# @Title: 柠檬水找零 (Lemonade Change)
# @Author: qinxinlei
# @Date: 2018-10-23 15:19:38
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        i=0
        j=0
        for bill in bills:
            if bill==5:
                i+=1
            elif bill==10:
                if i>0:
                    i-=1
                    j+=1
                else:
                    return False
            else:
                if j>0 and i>0:
                    j-=1
                    i-=1
                elif i>2:
                    i-=3
                else:
                    return False
        return True
