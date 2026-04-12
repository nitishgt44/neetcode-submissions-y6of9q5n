class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictVal1={}
        list1 = []
        for i in nums1:
            dictVal1[i] = dictVal1.get(i,0)+1
        
        for i in nums2:
            for key,val in dictVal1.items():
                if i == key:
                    if i not in list1:
                        list1.append(key)

        return list1

        