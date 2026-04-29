class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        dictVal = {}
        minVal = 101
        for i in nums:
            dictVal[i] = dictVal.get(i,0)+1
        # print(dictVal)
        list1 = []

        count = 1 
        while count <= len(dictVal):
            minVal = 101
            minKey = None
            for k,v in dictVal.items():
                # print("minVal",minVal)
                # print("minKey",minKey)
                if minKey!= None:
                    if v < minVal:
                        minVal = v
                        minKey = k
                    elif v == minVal:
                        if k > minKey:
                            minKey = k
                            minVal = v
                else:
                    if v < minVal:
                        minVal = v
                        minKey = k
            # print(minVal)
            # print(minKey)
            for i in range(minVal):
                list1.append(minKey)
            dictVal[minKey] = 1001
            count+=1

        return (list1)


        