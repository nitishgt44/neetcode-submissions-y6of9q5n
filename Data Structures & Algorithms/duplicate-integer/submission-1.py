class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dictVal = {}

        for i in nums:
            dictVal[i] = dictVal.get(i,0)+1

        for k,v in dictVal.items():
            if v > 1:
                return True
        return False

        