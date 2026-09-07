# Longest Subarray of 1's After Deleting One Element

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 
Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.


Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].


Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


 
Constraints:


	1 <= nums.length <= 105
	nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-07T09:07:58.377Z  

```py
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


        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)