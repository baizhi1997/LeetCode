
# @Title: 将每个元素替换为右侧最大元素 (Replace Elements with Greatest Element on Right Side)
# @Author: qinxinlei
# @Date: 2020-07-28 15:33:57
# @Runtime: 100 ms
# @Memory: 14.3 MB

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            arr[i], tmp = tmp, max(arr[i], tmp)
        return arr            
