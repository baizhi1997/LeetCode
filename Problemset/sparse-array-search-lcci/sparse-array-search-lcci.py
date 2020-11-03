
# @Title: 稀疏数组搜索 (Sparse Array Search LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 14:33:48
# @Runtime: 44 ms
# @Memory: 13.6 MB

class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            mid = left + (right - left) // 2
            temp = mid
            while words[mid] == '' and mid < right:
                mid += 1
            if words[mid] == '':
                right = temp - 1
                continue
            
            if words[mid] == s:
                return mid
            elif s < words[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
