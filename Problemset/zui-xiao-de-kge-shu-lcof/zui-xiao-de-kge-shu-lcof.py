
# @Title: 最小的k个数 (最小的k个数  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 10:52:54
# @Runtime: 800 ms
# @Memory: 23.5 MB

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        l, r = [], []
        for n in arr[1:]:
            if n < arr[0]:
                l.append(n)
            else:
                r.append(n)
        x = len(l)
        if x >= k:
            return self.getLeastNumbers(l, k)
        elif x == k-1:
            return l + [arr[0]]
        return l + [arr[0]] +self.getLeastNumbers(r, k-x-1) 
        
