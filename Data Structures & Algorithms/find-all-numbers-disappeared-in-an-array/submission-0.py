class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        dictVal = {}
        list1=[]
        for i in nums:
            dictVal[i] = dictVal.get(i,0)+1

        for j in range(1,n+1):
            try:
                x = dictVal[j]  
            except:
                list1.append(j)

        return list1

        