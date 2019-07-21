class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenArray=[]
        
        
        if len (s)==0:
            return 0
        self.helper (0,s, lenArray) 
        lenArray.sort ()
       
        array_size=len (lenArray) -1
        
        return lenArray[array_size]
        
            
            
        
    def helper (self,index, s, lenArray):
        cur_string_len=0
        cur_string=[]
       
        for x in range (index,len (s)):
            
            
            if s[x] not in cur_string:
                cur_string_len+=1
                cur_string+=s[x]
            else:
                if cur_string_len not in lenArray:
                    lenArray.append (cur_string_len)
                self.helper (x, s, lenArray)
                return 
        if cur_string_len not in lenArray:
            lenArray.append (cur_string_len)
         
        
                
            
            
            
        
        
            
            
        
        
   
        
        
        
    
        
        