
# @Title: 长按键入 (Long Pressed Name)
# @Author: qinxinlei
# @Date: 2018-11-08 17:22:30
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i=j=0
        pre=' '
        l1=len(name)
        l2=len(typed)
        while i<l1 and j<l2:
            if name[i]==typed[j]:
                pre=name[i]
                i+=1
                j+=1
            else:
                if typed[j]!=pre:
                    return False
                else:
                    j+=1
        return i==l1
