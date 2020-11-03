
# @Title: 有多少小于当前数字的数字 (How Many Numbers Are Smaller Than the Current Number)
# @Author: qinxinlei
# @Date: 2020-07-28 13:46:02
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tmp = sorted(nums)
        dic = {}
        for i in range(len(tmp)):
            if tmp[i] not in dic:
                dic[tmp[i]] = i
        return [dic[num] for num in nums]
