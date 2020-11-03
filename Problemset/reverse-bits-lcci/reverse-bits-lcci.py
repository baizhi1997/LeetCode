
# @Title: 翻转数位 (Reverse Bits LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 11:33:37
# @Runtime: 28 ms
# @Memory: 13.4 MB

class Solution:
    def reverseBits(self, num: int) -> int:
        pre, cur = 0, 0
        ans = 0
        for i in range(32):
            if num & (1 << i):
                cur += 1
            else:
                ans = max(ans, pre + cur)
                pre = cur + 1
                cur = 0
        ans = max(ans, pre + cur)
        return ans
