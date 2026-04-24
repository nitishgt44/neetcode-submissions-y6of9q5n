class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        n1 = len(word1)
        n2 = len(word2)
        max = ""
        if len(word1)> len(word2):
            diff = n1-n2
            maxVal = word1
            maxLen = n2
        else:
            diff = n2-n1
            maxVal = word2
            maxLen = n1
        
        for i,j in zip(word1,word2):
            string+=i
            string+=j

        for i in maxVal[maxLen:]:
            string+=i
        return string

        