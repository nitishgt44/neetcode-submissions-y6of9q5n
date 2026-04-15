class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        list1 = []
        dictVal = {}

        for i in arr:
            dictVal[i] = dictVal.get(i,0)+1
        # print(dictVal)
        for key,val in dictVal.items():
            if val >1:
                pass
            else:
                list1.append(key)
        # print(list1)
        try:
            return list1[k-1]
        except:
            return ""

        