from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_count = dict ()
        for i in nums:
            if i in nums_count:
                nums_count[i]= nums_count.get(i) +1
            else:
                nums_count[i]=1
        print (nums_count)
        highest= sorted (nums_count.values (), reverse=True)
        highest= highest[0:k]
        final=[]
        i=0
        for key, value in nums_count.items():
            if i==k:
                break
            if value in highest:
                final.append (key)
                i+=1
        return final
            
                
        
        
     
