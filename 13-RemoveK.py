"""
Given a non-negative integer num represented as a string, 
remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

"""

#Solution

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        n=len(num)-k
        for i in range(0,len(num)):
                while len(stack)>0 and stack[-1]>int(num[i]) and k>0  :
                    stack.pop()
                    k-=1

                stack.append(int(num[i]))
        m=0
        for i in range(n):
            m+=10**(n-i-1)*stack[i]
        return str(m)
