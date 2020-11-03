
# @Title: 森林中的兔子 (Rabbits in Forest)
# @Author: qinxinlei
# @Date: 2018-11-23 21:29:34
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dic=collections.Counter(answers)
        ans=0
        for i in dic:
            x,y=divmod(dic[i],i+1)
            if y:
                ans+=(x+1)*(i+1)
            else:
                ans+=dic[i]
        return ans
