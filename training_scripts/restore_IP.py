
class Solution:
    def restoreIPAddresses(self,s: str) -> List[str]:
        result=[]
        if len(s)>12 or len(s)<4:
            return result
        def backtrack(index,numDots,currIP):
            if numDots == 4 and index == len(s):
                result.append(currIP[:-1])
                return
            if numDots > 4:
                return
            for j in range (index, min(index+3,len(s))):
                if int(s[index:j+1])<256 and (index == j or not s[index]=="0"):
                    backtrack(j+1,numDots+1, currIP+s[index:j+1]+".")
        backtrack(0,0,"")
        return result