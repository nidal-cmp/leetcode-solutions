class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maximum=max(candies)
        result = []

        for x in candies:
            if x + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result