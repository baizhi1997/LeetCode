
# @Title: 重新排列日志文件 (Reorder Data in Log Files)
# @Author: qinxinlei
# @Date: 2018-11-16 20:15:56
# @Runtime: 56 ms
# @Memory: N/A

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits=[]
        letters=[]
        for log in logs:
            if log[-1].isalpha():
                letters.append(log)
            else:
                digits.append(log)
        letters.sort(key=lambda x:x[x.find(' '):])
        return letters+digits
