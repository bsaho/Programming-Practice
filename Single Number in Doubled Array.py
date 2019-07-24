class Solution(object):
    def singleNumber(self, nums):        
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort ()
        counter=1
        for i in range (1, len (nums)):
            print (i, counter)
            if i == 1:
                if nums[i] != nums[i-1]:
                    return nums[i-1]
                else: 
                    counter = 0
            else:    
                if nums[i] != nums[i-1] and counter==1:
                    return nums[i]
                elif nums[i] != nums[i-1] and counter==0:
                    counter=1
                elif nums[i] == nums[i-1]:
                    counter=0
        if counter==0:
            return nums[len(nums)-1]
         
        print (nums)
            
                