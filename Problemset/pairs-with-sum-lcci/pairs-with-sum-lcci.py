
# @Title: 数对和 (Pairs With Sum LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 20:46:42
# @Runtime: 212 ms
# @Memory: 32.4 MB

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        dic = collections.Counter()
        ans = []
        for num in nums:
            if dic[num] > 0:
                dic[num] -= 1
                ans.append([num, target-num])
            else:
                dic[target-num] += 1
        return ans
