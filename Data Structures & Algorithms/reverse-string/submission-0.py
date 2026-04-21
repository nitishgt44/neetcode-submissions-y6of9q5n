class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)//2

        # print(n)
        topVal = -1
        bottomVal = 0
        for i in range(n):
            # print(s[bottomVal])
            # print(s[topVal])
            s[bottomVal],s[topVal] = s[topVal],s[bottomVal]
            bottomVal+=1
            topVal-=1
        