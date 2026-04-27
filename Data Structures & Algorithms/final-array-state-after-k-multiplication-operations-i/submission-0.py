class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        
        minIndex = None
        count = 1
        while count <= k:
            minVal = 101
            for index,val in enumerate(nums):
                if val < minVal:
                    minVal = val
                    minIndex = index
                    # print(minIndex)
            nums[minIndex] *= multiplier
            # print(nums)
            count+=1
        return (nums)
            
        
        