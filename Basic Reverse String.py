class Solution(object):
    def reverseString(self, s):
        
        if len (s) % 2 ==1:
           
            for i in range (0,len (s)):
                
                wordBuffer= s[i]
                if i != (len (s) // 2):
                    s[i]= s[(len (s) -1) -i]
                    s[(len (s)-1) -i] = wordBuffer
                else: 
                    break
        else:
            for i in range (0,len (s)):
                wordBuffer= s[i]
                
                s[i]= s[(len (s)-1) -i]
                s[(len (s)-1) -i]= wordBuffer
                if i == (len (s) // 2) -1:
                    break
                    
                
        
            
            
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        