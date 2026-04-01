class Solution:
    def search(self, nums: List[int], target: int) -> int:
        val = None
        for i in range(len(nums)):
            if nums[i] == target:
                val = i
                print(val)
                break
        if val!=None:
            return val
        else:
            return -1
                
        
        