# Unique Number of Occurrences

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 
Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false


Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


 
Constraints:


	1 <= arr.length <= 1000
	-1000 <= arr[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.5 MB  
**Submitted:** 2026-08-31T09:10:22.429Z  

```py
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)

        answer1 = []
        answer2 = []


        for num in set1:
            if num not in set2:
                answer1.append(num)
        
        for num in set2:
            if num not in set1:
                answer2.append(num)
        
        return [answer1,answer2]

```

---

[View on LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/)