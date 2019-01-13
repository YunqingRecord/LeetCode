class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num = 0
        i = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                num += 1
        if len(flowerbed) == 2:
            if flowerbed[0] == flowerbed[1] == 0:
                num += 1
        if len(flowerbed) >= 3:
            if flowerbed[0] == flowerbed[1] == 0:
                num += 1
                flowerbed[0] = 1
            if flowerbed[-1] == flowerbed[-2] == 0:
                num += 1
                flowerbed[-1] = 1
            while i < len(flowerbed) - 1:
                if flowerbed[i] == 0:
                    if flowerbed[i - 1] == flowerbed[i + 1] == 0:
                        num += 1
                        flowerbed[i] = 1
                    else:
                        i += 2
                elif flowerbed[i] == 1:
                    i += 2
        if num >= n:
            return True
        else:
            return False


def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    num = 0
    i  = 0
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            num += 1
            if num >= n:
                return True
    if len(flowerbed) == 2:
        if flowerbed[0] == flowerbed[1] == 0:
            num += 1
            if num >= n:
                return True
    if len(flowerbed) >= 3:
        if flowerbed[0] == flowerbed[1] == 0:
            num += 1
            flowerbed[0] = 1
            if num >= n:
                return True
        if flowerbed[-1] == flowerbed[-2] == 0:
            num += 1
            flowerbed[-1] = 1
            if num >= n:
                return True
        while i < len(flowerbed)-1:
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == flowerbed[i + 1] == 0:
                    num += 1
                    flowerbed[i] = 1
                    if num >= n:
                        return True
                else:
                    i += 2
            elif flowerbed[i] == 1:
                i += 2
    if num == n:
        return True
    else:
        return False


flowerbed = [1,0,1,0,1,0,1]
n = 0

print(canPlaceFlowers(flowerbed= flowerbed, n=n))

