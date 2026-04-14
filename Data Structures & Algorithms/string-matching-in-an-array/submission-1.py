class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        # n = len(patterns)
        list1=[]
        for index,val in enumerate(words):
            currentVal = words.pop(index)
            # print(currentVal)
            for i in words:
                if currentVal in i:
                    if currentVal in list1:
                        pass
                    else:
                        list1.append(currentVal)
                    # print(currentVal)
            words.insert(index,currentVal)
        return list1
        