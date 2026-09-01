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