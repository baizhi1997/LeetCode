
# @Title: 按既定顺序创建目标数组 (Create Target Array in the Given Order)
# @Author: qinxinlei
# @Date: 2020-07-28 13:41:02
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.insert(index[i], nums[i])
        return ret

