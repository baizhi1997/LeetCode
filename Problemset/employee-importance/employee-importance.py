
# @Title: 员工的重要性 (Employee Importance)
# @Author: qinxinlei
# @Date: 2018-10-31 21:48:10
# @Runtime: 208 ms
# @Memory: N/A

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ans=0
        dic={i.id:i for i in employees}
        q=[id]
        while q:
            i=dic[q.pop()]
            ans+=i.importance
            q+=i.subordinates
        return ans
