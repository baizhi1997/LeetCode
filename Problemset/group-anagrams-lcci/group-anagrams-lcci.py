
# @Title: 变位词组 (Group Anagrams LCCI)
# @Author: qinxinlei
# @Date: 2020-06-22 23:11:42
# @Runtime: 64 ms
# @Memory: 16.1 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        return list(dic.values())
