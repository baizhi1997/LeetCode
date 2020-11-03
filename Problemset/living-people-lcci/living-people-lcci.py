
# @Title: 生存人数 (Living People LCCI)
# @Author: qinxinlei
# @Date: 2020-06-19 15:16:36
# @Runtime: 64 ms
# @Memory: 14 MB

class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        dic1 = collections.Counter(birth)
        dic2 = collections.Counter(death)
        ans = 1899
        max_people = 0
        tmp_people = 0
        for i in range(1900, 2001):
            tmp_people = tmp_people + dic1[i] - dic2[i-1]
            if tmp_people > max_people:
                max_people = tmp_people
                ans = i
        return ans
