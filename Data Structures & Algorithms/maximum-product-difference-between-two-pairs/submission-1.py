class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        maxVal = 0
        minVal = 10000*10000
        
        for i in range(0,len(nums)):
            mult = 1
            for j in range(i+1,len(nums)):
                mult = nums[i]*nums[j]
                # print(mult)
                if mult> maxVal:
                    maxVal = mult
                    print(maxVal)
                if mult<minVal:
                    minVal = mult
                    print(minVal)
        return maxVal - minVal
                
        