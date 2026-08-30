class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0

        for num in nums:
            needed = k - num
            
            if count.get(needed,0) > 0:
                operations += 1
                count[needed] -= 1
            else:
                count[num] = count.get(num,0) + 1
        return operations