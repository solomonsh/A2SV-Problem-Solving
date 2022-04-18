"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total_importance = 0
       
        def getEmployee(employees,id):
            for emp in employees:
                if emp.id == id:
                    return emp
                
        def calculateTotalImportance(root):
            self.total_importance += root.importance
            for sub in root.subordinates:
                calculateTotalImportance(getEmployee(employees,sub))
            
        
            
        for emp in employees:
            if emp.id == id:
                  print(emp.importance,emp.subordinates)
                  calculateTotalImportance(emp)
                

        return self.total_importance
            
            
        