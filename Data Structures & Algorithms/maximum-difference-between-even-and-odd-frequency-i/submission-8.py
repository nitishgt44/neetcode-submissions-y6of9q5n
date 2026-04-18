class Solution:
    def maxDifference(self, s: str) -> int:

        dictVal = {}

        for i in s:
            dictVal[i] = dictVal.get(i,0)+1

        print(dictVal)
        
        evenMax = 0
        oddMax = 0
        evenMin = 101
        oddMin  = 101
        for k,v in dictVal.items():
            if v > evenMax and v%2 ==0:
                evenMax  = v
                # print(evenVal)
            elif v > oddMax and v%2!=0:
                oddMax = v
                # print(oddVal)

        for k,v in dictVal.items():
            if v < evenMin and v%2 ==0:
                evenMin  = v
                # print(evenVal)
            elif v < oddMin:
                oddMin = v
                # print(oddVal)
        print(evenMax)
        print(oddMax)
        print(evenMin)
        print(oddMin)


        # if oddMax - evenMin > evenMax- oddMin:
        #     print(oddMax - evenMin)
        #     return oddMax - evenMin
        # else:
        #     print(evenMax - oddMin)
        #     return evenMax - oddMin

        return oddMax - evenMin

