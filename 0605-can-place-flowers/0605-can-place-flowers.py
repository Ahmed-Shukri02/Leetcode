class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[max(i - 1, 0)] == flowerbed[i] == flowerbed[min(i + 1, len(flowerbed) - 1)] == 0:
                flowerbed[i] = 1
                n -= 1
                i += 1
            i += 1
        print(n)
        return n <= 0
            