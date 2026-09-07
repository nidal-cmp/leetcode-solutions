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
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-07T06:08:15.484Z  

```py
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = 'aeiou'
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count+=1
            
        max_count=count

        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1

            if s[i-k] in vowels:
                count-=1 

            max_count = max (max_count, count)

        return max_count

```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)