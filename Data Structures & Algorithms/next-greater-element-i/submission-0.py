class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        list1 = []
        for index,value in enumerate(nums1):
            indexVal = None
            for index1,value1 in enumerate(nums2):
                if value == value1:
                    indexVal = index1
                    for values in nums2[index1:]:
                        if values>value1:
                            list1.append(values)
                            break
                    else:
                        list1.append(-1)

        return list1

        