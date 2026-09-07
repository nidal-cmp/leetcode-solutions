class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        nz=0

        m_w=0

        for r in range(len(nums)):
             if nums[r] == 0:
               nz += 1
            
             while nz > k:
                 if nums[l] == 0:
                    nz -= 1
                 l += 1

             w = r - l + 1

             m_w = max(m_w,w)

        return m_w


        