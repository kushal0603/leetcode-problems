class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i, c in enumerate(s):
            d[c]=i
        highest=0  #highest index of element in string
        startindex=0  #index of start of each partition
        l=[]
        for currentind, c in enumerate(s):
            highest=max(highest,d[c]) #if included a element highest index position 
            
            if currentind==highest: #highest partition
                totalelements=currentind-startindex+1 #+1 to get length
                l.append(totalelements)
                
                startindex=currentind+1 #new starting index
        return l