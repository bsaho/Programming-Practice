from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countedNums= Counter (nums)
        countedNums= countedNums.most_common ()
        most_common= []
        for key,value in countedNums:
            if len (most_common) != k:
                most_common.append (key)
        return most_common
