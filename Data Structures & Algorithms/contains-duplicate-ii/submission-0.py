class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len (nums)
        boolean = False

        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    if i>j:
                        if i-j<=k:
                            boolean  = True
                    elif j>i:
                        if j-i <=k:
                            boolean = True
        return boolean

        