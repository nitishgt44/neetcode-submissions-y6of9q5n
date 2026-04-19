class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:


        n = len(grid)
        total = n*n
        # print(total)
        list1 = []
        dictVal = {}
    

        for i in grid:
            for k in i:
                dictVal[k] = dictVal.get(k,0) + 1
        print(dictVal)
        rep = None
        mis = None
        for k,v in dictVal.items():
            for j in range(1,total+1):
                if j not in dictVal:
                    mis = j
            if v > 1:
                rep = k

        list1.append(rep)
        list1.append(mis)

        return list1



        
