class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dictVal = {}
        boolean = False
        for i in nums:
            dictVal[i] = dictVal.get(i,0)+1
        
        for i in dictVal:
            if dictVal[i]>1:
                boolean = True
                break
        return boolean
        