class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        boolean = True
        
        while boolean:
            count = 0
            for index,value in enumerate(nums):
                if value == val:
                    nums.remove(value)
                    count+=1
                # print(nums)
            if count == 0:
                boolean = False 
        return len(nums)

       
        