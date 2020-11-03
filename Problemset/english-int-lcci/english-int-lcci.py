
# @Title: 整数的英语表示 (English Int LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 20:28:54
# @Runtime: 44 ms
# @Memory: 13.2 MB

class Solution:
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000, 1000000000]
    ss = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen","Seventeen", "Eighteen", "Nineteen","Twenty", "Thirty", "Forty", "Fifty","Sixty","Seventy", "Eighty", "Ninety","Hundred", "Thousand", "Million", "Billion"]
    k = 90
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'
        i = len(self.ns)-1
        while i>0 and self.ns[i]>num:
            i-=1
        n,s = self.ns[i],self.ss[i]
        pre = self.numberToWords(num//n)+' ' if n>self.k else ''
        suf = ' '+self.numberToWords(num%n) if num%n else ''
        return pre+s+suf

