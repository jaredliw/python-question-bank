class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Runtime: 136 ms
        # Memory: 13.8 MB
        count = 0
        for idx, plot in enumerate(flowerbed):
            if plot == 1:
                continue
            if idx > 0 and flowerbed[idx - 1]:
                continue
            if idx < len(flowerbed) - 1 and flowerbed[idx + 1]:
                continue
            flowerbed[idx] = 1
            count += 1
        if count >= n:
            return True
        else:
            return False


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Runtime: 128 ms
        # Memory: 14.2 MB
        count = 0
        if len(flowerbed) == 1 and not flowerbed[0]:
            count += 1
        else:
            if len(flowerbed) > 1 and not (flowerbed[0] or flowerbed[1]):
                flowerbed[0] = 1
                count += 1
            for idx in range(1, len(flowerbed) - 1):
                if flowerbed[idx - 1] == flowerbed[idx] == flowerbed[idx + 1] == 0:
                    flowerbed[idx] = 1
                    count += 1
            if len(flowerbed) > 1 and not (flowerbed[-1] or flowerbed[-2]):
                flowerbed[-1] = 1
                count += 1
        return count >= n