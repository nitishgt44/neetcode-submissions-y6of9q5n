class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        maj = n//2
        num = None

        dictVal = {}

        for i in nums:
            dictVal[i] = dictVal.get(i,0)+1

        for key, val in dictVal.items():
            if val > maj:
                maj = val
                num = key
        return num

        