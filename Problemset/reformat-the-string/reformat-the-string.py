
# @Title: 重新格式化字符串 (Reformat The String)
# @Author: qinxinlei
# @Date: 2020-08-02 21:28:09
# @Runtime: 72 ms
# @Memory: 13.3 MB

class Solution:
    def reformat(self, s: str) -> str:
        numbers=[]
        letters=[]
        for i in s:
            if i.isalpha():
                letters.append(i)
            else:
                numbers.append(i)
        n,l=len(numbers),len(letters)
        if abs(n-l)>1:
            return ''
        res=[]
        if n>=l:
            while numbers:
                res.append(numbers.pop())
                if letters:
                    res.append(letters.pop())
        else:
            while letters:
                res.append(letters.pop())
                if numbers:
                    res.append(numbers.pop())
        return "".join(res)

