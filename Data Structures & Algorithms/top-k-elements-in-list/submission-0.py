class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        output=[]
        for i in nums :
            if i not in d:
                d[i]=1
            else :
                d[i]+=1
        d=dict(sorted (d.items(),key=lambda x:x[1] , reverse =True))
        for j in d:
            if len(output)<k:
                output.append(j)
        return output
            
        
