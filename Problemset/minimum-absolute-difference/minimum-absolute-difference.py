
# @Title: 最小绝对差 (Minimum Absolute Difference)
# @Author: qinxinlei
# @Date: 2020-07-31 16:24:51
# @Runtime: 420 ms
# @Memory: 27 MB

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        tmp = float('inf')
        for i in range(len(arr)-1):
            if (d := arr[i+1] - arr[i]) < tmp:
                tmp = d
                ans = [[arr[i], arr[i+1]]]
            elif d == tmp:
                ans.append([arr[i], arr[i+1]])
        return ans    
