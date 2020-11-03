
# @Title: 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)
# @Author: qinxinlei
# @Date: 2018-11-05 21:03:23
# @Runtime: 156 ms
# @Memory: N/A

class Solution(object):   
    def findMedianSortedArrays(self, nums1, nums2):
        def getKth(A,B,k):
            l1=len(A)
            l2=len(B)
            if l1>l2:
                return getKth(B,A,k)
            if l1==0:
                return B[k-1]
            if k==1:
                return min(A[0],B[0])
            pa=min(k//2,l1)
            pb=k-pa
            if A[pa-1]<B[pb-1]:
                return getKth(A[pa:],B,pb)
            return getKth(A,B[pb:],pa)
        
        l1=len(nums1)
        l2=len(nums2)
        if (l1+l2)&1:
            return getKth(nums1,nums2,(l1+l2)//2+1)
        return (getKth(nums1,nums2,(l1+l2)//2)+getKth(nums1,nums2,(l1+l2)//2+1))/2
