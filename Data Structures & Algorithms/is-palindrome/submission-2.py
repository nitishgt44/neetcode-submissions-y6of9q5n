class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        list1 = list(s.replace(" ",""))
        for i in list1:
            if 65<=ord(i)<=90 or 97<=ord(i)<=122 or 48 <= ord(i) <= 57:
                pass
            else:
                list1.remove(i)
        # print(list1)
        # print(list1[::])
        # print(list1[::-1])
        n = len(list1)
        # print(n)
        minVal = 0
        maxVal = n
        if len(list1) == 0:
            return True
        else:
            boolean = True
            while minVal<=n//2:
                if list1[minVal].lower() == list1[maxVal-1].lower():
                    minVal+=1
                    maxVal-=1
                else:
                    boolean = False
                    break
            return boolean



        