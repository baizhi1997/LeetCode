
# @Title: 子域名访问计数 (Subdomain Visit Count)
# @Author: qinxinlei
# @Date: 2018-10-31 20:52:25
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans=collections.Counter()
        for domain in cpdomains:
            cnt,domain=domain.split()
            frags=domain.split('.')
            for i in range(len(frags)):
                ans['.'.join(frags[i:])]+=int(cnt)
        return ["{} {}".format(v,k) for k,v in ans.items()]
