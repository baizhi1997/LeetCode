
# @Title: 分数到小数 (Fraction to Recurring Decimal)
# @Author: qinxinlei
# @Date: 2019-05-24 11:44:46
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if n % d == 0: return str(n // d)
        p, q, r, s, m = abs(n), abs(d), abs(n) % abs(d), '', {}
        while r and r not in m: m[r], r, s = len(s), r * 10 % q, s + str(r * 10 // q)
        return ('' if (n > 0) == (d > 0) else '-') + str(p // q) + '.' + (s[:m[r]] + '(' + s[m[r]:] + ')' if r else s)
