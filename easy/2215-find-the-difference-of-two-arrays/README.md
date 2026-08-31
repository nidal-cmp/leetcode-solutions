# Find the Difference of Two Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:


	answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
	answer[1] is a list of all distinct integers in nums2 which are not present in nums1.


Note that the integers in the lists may be returned in any order.

 
Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].

Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].


 
Constraints:


	1 <= nums1.length, nums2.length <= 1000
	-1000 <= nums1[i], nums2[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.4 MB  
**Submitted:** 2026-08-31T08:47:15.906Z  

```py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]

            if right == left:

               return i
            
            left += nums[i]

        return -1
        
```

---

[View on LeetCode](https://leetcode.com/problems/find-the-difference-of-two-arrays/)