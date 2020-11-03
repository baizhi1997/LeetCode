
# @Title: 字符串转换整数 (atoi) (String to Integer (atoi))
# @Author: qinxinlei
# @Date: 2018-09-30 17:28:34
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        tmp=str.strip()
        p=re.compile("(^[\+\-]?[0]?\d+)\D*")
        tmp=p.findall(tmp)
        if not tmp:
            return 0
        output="".join(tmp)
        output_int=int(output)
        limit=pow(2,31)
        output_int=max(output_int,-limit)
        output_int=min(output_int,limit-1)
        return output_int
    
