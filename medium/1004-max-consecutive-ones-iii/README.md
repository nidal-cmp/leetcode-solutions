# Max Consecutive Ones III

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


 
Constraints:


	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
	0 <= k <= nums.length

## Solution

**Language:** Python  
**Runtime:** 51 ms (beats 85.55%)  
**Memory:** 22.1 MB (beats 51.06%)  
**Submitted:** 2026-09-07T06:26:53.677Z  

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

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)