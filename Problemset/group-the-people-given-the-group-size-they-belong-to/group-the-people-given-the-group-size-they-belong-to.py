
# @Title: 用户分组 (Group the People Given the Group Size They Belong To)
# @Author: qinxinlei
# @Date: 2020-06-02 00:09:23
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dic:
                dic[groupSizes[i]] = [i]
            else:
                dic[groupSizes[i]].append(i)
        ans = []
        for k, v in dic.items():
            for i in range(0, len(v), k):
                ans.append(v[i:i+k])
        return ans
                
