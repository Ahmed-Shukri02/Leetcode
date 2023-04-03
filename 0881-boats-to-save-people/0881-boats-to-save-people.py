class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l, r = 0, len(people) - 1
        f = 0
        while l < r:
            if people[l] + people[r] <= limit:
                f += 1
                l, r = l + 1, r - 1
            else:
                f, r = f + 1, r - 1

        if l == r: f += 1

        return f

