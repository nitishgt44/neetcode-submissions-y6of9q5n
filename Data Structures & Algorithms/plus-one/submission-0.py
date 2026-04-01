class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sumVal = 0 
        str1 = ""
        for i in digits:
            str1+=(str(i))
        # print(str1)

        val = int(str1)+1
        # print(val)
        list1 = list(str(val))
        list2 = []
        for i in list1:
            list2.append(int(i))

        return (list2)

        