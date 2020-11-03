
# @Title: 长度为 n 的开心字符串中字典序第 k 小的字符串 (The k-th Lexicographical String of All Happy Strings of Length n)
# @Author: qinxinlei
# @Date: 2020-06-17 10:13:07
# @Runtime: 44 ms
# @Memory: 13.3 MB

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        c = ['a','b','c']
        d = {'a':['b','c'],'b':['a','c'],'c':['a','b']}
        n = n - 1
        k = k - 1
        maxnum = 2 ** n * 3 - 1
        if k > maxnum:
            return ''
        index,k = k // (2 ** n),k % (2 ** n)
        res = c[index]
        while n != 0:
            n = n - 1
            index,k = k // (2 ** n),k % (2 ** n)
            res = res + d[res[-1]][index]
        return res

