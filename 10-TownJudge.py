"""
In a town, there are N people labelled from 1 to N.  
There is a rumor that one of these people is secretly the town judge.


If the town judge exists, then: 

The town judge trusts nobody.

Everybody (except for the town judge) trusts the town judge.

There is exactly one person that satisfies properties 1 and 2.


You are given trust, an array of pairs trust[i] = [a, b] representing 
that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  

Otherwise, return -1.

"""
#Solution 

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        people=[x for x in range(1,N+1)]
        l= []
        
        for i in range(len(trust)):
            l.append(trust[i][0])
            
        print((set(people)-set(l)))
        count = 0 
        if (set(people)-set(l))==set():    
            return -1
        else:
            s=list(set(people)-set(l))
            for j in range(len(trust)):
                if trust[j][1]==s[0]:
                    count+=1
            
            if count == N-1:
                return s[0]
            
            else:
                return -1
