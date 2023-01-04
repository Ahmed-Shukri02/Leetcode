class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # get counts
        hmap = {}
        for task in tasks:
            hmap[task] = hmap.get(task, 0) + 1
        final = 0
        for t in hmap.values():
            if t < 2:
                return -1
            three = two = mix = float("inf")
            if t % 2 == 0:
                two = t // 2
            if t % 3 == 0:
                three = t // 3
            mix = (t // 3) + ((t % 3)//2)
            if t % 3 == 1:
                mix += 1

            final += min(three, two, mix)
        return final