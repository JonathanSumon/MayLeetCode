"""
Given a circular array C of integers represented by A, 
find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects 
to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, 
and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer 
A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], 
there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
"""



#Solution

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        
        maxTotal,maxSoFar,minSoFar,minTotal,s = A[0], A[0], A[0], A[0],A[0]
        
        for i in range(1, len(A)):
            maxSoFar = max(A[i], maxSoFar + A[i])
            maxTotal = max(maxTotal, maxSoFar)            
            
            minSoFar = min(A[i], minSoFar + A[i])            
            minTotal = min(minTotal, minSoFar)            
            s += A[i]
        if(s == minSoFar):
            return maxTotal
        
        return max(s - minTotal, maxTotal);