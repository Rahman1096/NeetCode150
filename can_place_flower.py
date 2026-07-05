class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i  in range(len(flowerbed)):
            if flowerbed[i]:
                continue
            # if next is valid index and also 0 (free plot)
            elif i+1<len(flowerbed) and i+2<len(flowerbed)and not flowerbed[i+1] and flowerbed[i+2]:
                n -=1
                flowerbed[i+1]=1
                i +=1
        #if n becomes zero return true
        if not n:
            return True
        else:
            return False