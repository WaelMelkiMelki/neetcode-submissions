class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictio={}

        for i in s :
            if i in dictio:
                dictio[i]+=1
            else:
                dictio[i]=1
        for j in t:
            if j in dictio:
                dictio[j]-=1
            else:
                dictio[j]=-1
        for k in dictio.values():
            if k!= 0:
                return False
        return True