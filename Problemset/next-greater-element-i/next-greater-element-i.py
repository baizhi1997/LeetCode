
# @Title: 下一个更大元素 I (Next Greater Element I)
# @Author: qinxinlei
# @Date: 2018-10-22 11:27:14
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic={}
        stack=[]
        for i in nums2:
            while stack and stack[-1] < i:
                dic[stack.pop()] = i
            stack.append(i)
        return [dic.get(i, -1) for i in nums1]
    
