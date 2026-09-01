# Equal Row and Column Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 
Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]


Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


 
Constraints:


	n == grid.length == grid[i].length
	1 <= n <= 200
	1 <= grid[i][j] <= 105

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.1 MB  
**Submitted:** 2026-09-01T11:53:34.516Z  

```py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        count = {}

        if set(word1) != set(word2):
           
           return False
        
        count1 = {}
        count2 = {}

        for char in word1:
            count1[char]=count1.get(char,0)+1

        for char in word2:
            count2[char]=count2.get(char,0)+1

        return sorted(count1.values()) == sorted(count2.values())
```

---

[View on LeetCode](https://leetcode.com/problems/equal-row-and-column-pairs/)