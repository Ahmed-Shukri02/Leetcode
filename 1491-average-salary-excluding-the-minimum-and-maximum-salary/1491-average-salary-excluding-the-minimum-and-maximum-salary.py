class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)[1:-1]
        return sum(salary)/len(salary)