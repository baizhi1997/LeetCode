
# @Title: 运算 (Operations LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 19:31:08
# @Runtime: 124 ms
# @Memory: 13.7 MB

class Operations:
    def __init__(self):
        pass

    def calSign(self, a, b):
        pos = True
        if a < 0:
            pos = not pos
            a = self.minus(0, a)
        if b < 0:
            pos = not pos
            b = self.minus(0, b)
        return (a, b, pos)

    def minus(self, a: int, b: int) -> int:
        # 位运算做法 - 取反+1
        return a + ~b + 1

    def multiply(self, a: int, b: int) -> int:
        # 使用位运算的做法 - 二进制乘法, 类似十进制乘法
        a, b, pos = self.calSign(a, b)
        i = 0
        res = 0
        while b > 0:
            if b & 1:
                res += a << i
            i += 1
            b >>= 1
        return res if pos else self.minus(0, res)

        # 也可以递归, 相同思路
        a, b, pos = self.calSign(a, b)

        def multi(a, b):
            if not b:
                return 0
            return multi(a, b >> 1) << 1 + (a if b & 1 else 0)

        res = multi(a, b)
        return res if pos else self.minus(0, res)

    def divide(self, a: int, b: int) -> int:
        # 二进制除法, 使用一个变量保存被除数, 对该变量一直向左移位, 直到其<<1大于a为止, 然后res加上对应的倍数, a减去该变量的值, 直到a<b
        a, b, pos = self.calSign(a, b)
        i = 0
        res = 0
        while a >= b:
            curb = b
            times = 1
            while a >= curb << 1:
                curb <<= 1
                times <<= 1
            res += times
            a = self.minus(a, curb)
        return res if pos else self.minus(0, res)


# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
