
# @Title: 解压缩编码列表 (Decompress Run-Length Encoded List)
# @Author: qinxinlei
# @Date: 2020-07-28 13:37:04
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)//2):
            ans.extend([nums[i*2+1]]*nums[i*2])
        return ans
