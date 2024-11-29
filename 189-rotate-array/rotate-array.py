class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        myarr=[0]*len(nums)

        
        for i in range(0,len(nums)):
            pos=(i+k)%len(nums)
            myarr[pos]=nums[i]
        nums[:]=myarr
        return nums
