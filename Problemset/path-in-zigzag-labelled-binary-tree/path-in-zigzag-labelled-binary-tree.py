
# @Title: 二叉树寻路 (Path In Zigzag Labelled Binary Tree)
# @Author: qinxinlei
# @Date: 2019-07-02 10:40:52
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        x = int(math.log(label, 2))
        tmp = 3 * pow(2, x) 
        ans = [label]
        pre = label
        for _ in range(x):
            pre = (tmp - pre - 1) // 2
            ans.append(pre)
            tmp //= 2
        return ans[::-1]
