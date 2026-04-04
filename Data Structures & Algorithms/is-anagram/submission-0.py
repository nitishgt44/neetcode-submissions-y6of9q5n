class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictVal1 = {}
        dictVal2 = {}
        for i in s:
            dictVal1[i] = dictVal1.get(i,0)+1

        for j in t:
            dictVal2[j] = dictVal2.get(j,0)+1

        if dictVal1 == dictVal2:
            return True
        else:
            return False

        