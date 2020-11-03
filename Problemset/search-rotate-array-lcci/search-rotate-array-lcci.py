
# @Title: 搜索旋转数组 (Search Rotate Array LCCI)
# @Author: qinxinlei
# @Date: 2020-07-18 22:16:17
# @Runtime: 40 ms
# @Memory: 14.3 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[left] < nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[left] <= target or target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[left] == nums[mid]:
                if nums[left] != target:
                    left += 1                                        
                else:
                    right = left
        return left if nums[left] == target else -1

