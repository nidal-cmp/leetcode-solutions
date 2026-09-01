# Removing Stars From a String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string s, which contains stars *.

In one operation, you can:


	Choose a star in s.
	Remove the closest non-star character to its left, as well as remove the star itself.


Return the string after all stars have been removed.

Note:


	The input will be generated such that the operation is always possible.
	It can be shown that the resulting string will always be unique.


 
Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.


 
Constraints:


	1 <= s.length <= 105
	s consists of lowercase English letters and stars *.
	The operation above can be performed on s.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.2 MB  
**Submitted:** 2026-09-01T12:21:30.852Z  

```py
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {}

        for row in grid:
            row = tuple(row)
            count[row] = count.get(row,0)+1
        
        answer = 0

        n = len(grid)
        
         
        
        for col in range(n):
            column = []

            for row in range(n):
                column.append(grid[row][col])
            
            column = tuple(column)

            answer += count.get(column,0)

        return answer


         

        
```

---

[View on LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/)