
# @Title: 独特的电子邮件地址 (Unique Email Addresses)
# @Author: qinxinlei
# @Date: 2018-11-17 11:15:50
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        set1=set()
        for email in emails:
            local,domain=email.split('@',1)
            local=local.replace('.','').split('+')[0]
            set1.add(local+domain)
        return len(set1)
