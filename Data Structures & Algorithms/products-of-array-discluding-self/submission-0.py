class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        count = 0
        list1 = []
        
        while count<=len(nums)-1:
            for index,value in enumerate(nums):
                multiplier = 1
                swap = nums[count]
                nums[count] = 1
                # print(swap)
                for val in nums:
                    # print(val)
                    multiplier *= val
                # print(multiplier)
                list1.append(multiplier)
                nums[count] = swap
                count+=1
        return list1
        

        