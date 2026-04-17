class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        final = 0
        for i in nums:
            if i ==1:
                counter+=1
                if counter>final:
                    final = counter
            else:
                if final>counter:
                    pass
                else:
                    final = counter
                counter=0
        
        return final
                

        