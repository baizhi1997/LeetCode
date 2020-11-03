
# @Title: 求众数 II (Majority Element II)
# @Author: qinxinlei
# @Date: 2018-10-08 19:54:50
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1,num2=0,1
        cnt1,cnt2=0,0
        for num in nums:
            if num==num1:
                cnt1+=1
            elif num==num2:
                cnt2+=1
            elif cnt1==0:
                num1=num
                cnt1=1
            elif cnt2==0:
                num2=num
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        l=len(nums)//3
        return [num for num in (num1,num2) if nums.count(num)>l]
