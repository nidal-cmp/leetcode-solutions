# Maximum Number of Vowels in a Substring of Given Length

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.


Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.


Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


 
Constraints:


	1 <= s.length <= 105
	s consists of lowercase English letters.
	1 <= k <= s.length

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-07T05:37:46.166Z  

```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum = window_sum + nums[i]
            window_sum = window_sum - nums[i-k]

            max_sum = max(max_sum,window_sum)

        return max_sum/k
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)