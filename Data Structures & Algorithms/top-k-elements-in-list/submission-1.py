class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictVal = {}

        for i in nums:
            dictVal[i] = dictVal.get(i,0)+1
        list1 = []
        count = 1
        while count<=k:
            maxVal = 0
            maxKey = -1001
            for key,value in dictVal.items():
                if value > maxVal:
                    maxVal = value
                    maxKey = key
            # print(maxKey,maxVal)
            list1.append(maxKey)
            del dictVal[maxKey]
            count+=1
        return(list1)