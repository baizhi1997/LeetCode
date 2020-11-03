
# @Title: 字母异位词分组 (Group Anagrams)
# @Author: qinxinlei
# @Date: 2018-10-01 21:52:41
# @Runtime: 124 ms
# @Memory: N/A

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic=collections.defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            dic[key].append(s)
        return list(dic.values())
