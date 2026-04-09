class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        list1 = s.split(" ")
        list2 = []
        for i in list1:
            if len(i)>=1 and i != "":
                list2.append(i)
        # print(list2)
        return len(list2[-1])

        