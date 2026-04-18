class Solution:
    def findLucky(self, arr: List[int]) -> int:

        dictVal = {}
        list1 = []
        value = 0
        for i in arr:
            dictVal[i]  =dictVal.get(i,0)+1

        for key,val in dictVal.items():
            if key == val:
                list1.append(key)

        if len(list1) == 0:
            return -1
        elif len(list1)>1:
            for i in list1:
                if i > value:
                    value = i
            return value
        else:
            return list1[0]
        
        