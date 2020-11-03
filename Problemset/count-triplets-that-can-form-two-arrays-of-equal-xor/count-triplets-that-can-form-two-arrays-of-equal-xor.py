
# @Title: 形成两个异或相等数组的三元组数目 (Count Triplets That Can Form Two Arrays of Equal XOR)
# @Author: qinxinlei
# @Date: 2020-06-24 22:29:39
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = collections.Counter({0: 1})
        minus = collections.Counter()
        ans = 0
        cur_xor = 0
        for right in range(len(arr)):
            cur_xor ^= arr[right]
            ans += right * count[cur_xor] - minus[cur_xor]
            count[cur_xor] += 1
            minus[cur_xor] += (right + 1)
        return ans
