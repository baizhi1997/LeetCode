
# @Title:  字母与数字 (Find Longest Subarray LCCI)
# @Author: qinxinlei
# @Date: 2020-07-16 21:03:00
# @Runtime: 256 ms
# @Memory: 23.3 MB

class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        set1 = set("1234567890")
        cnt = 0
        dic = {0: -1}
        maxl = 0
        ans = []
        for i in range(len(array)):
            cnt += 1 if array[i][0] in set1 else -1
            if cnt not in dic:
                dic[cnt] = i
            elif i - dic[cnt] > maxl:
                maxl = i - dic[cnt]
                ans = [dic[cnt], i]
        if not ans:
            return []
        return array[ans[0]+1:ans[1]+1]
