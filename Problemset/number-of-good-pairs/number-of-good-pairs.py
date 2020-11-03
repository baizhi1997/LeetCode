
# @Title: 好数对的数目 (Number of Good Pairs)
# @Author: qinxinlei
# @Date: 2020-07-28 12:01:09
# @Runtime: 36 ms
# @Memory: 13.2 MB

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        ans = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                ans += dic[num]
                dic[num] += 1
        return ans
