class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for index in range(len(arr)-1):
            maxVal = 0 
            for index1 in range(index+1,len(arr)):
                if arr[index1]>maxVal:
                    maxVal = arr[index1]
            arr[index] = maxVal

        arr[-1] = -1

        return(arr)
            