
# @Title: 比较版本号 (Compare Version Numbers)
# @Author: qinxinlei
# @Date: 2019-05-24 11:14:12
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:        
        l1 = [int(v) for v in version1.split('.')]
        l2 = [int(v) for v in version2.split('.')]
        for i in range(max(len(l1), len(l2))):
            v1 = l1[i] if i < len(l1) else 0
            v2 = l2[i] if i < len(l2) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1  
        return 0
