"""

Given a positive integer, output its complement number. The complement strategy is 
to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.

"""

class Solution:
    def findComplement(self, num: int) -> int:
        num=bin(num)
        num = num[2:]
        a='0b'
        for i in range(len(num)):
            print(num[i])
            if num[i]=='1':
                a+='0'  
            elif num[i]=='0':
                a+='1'
            else:
                pass
            
        return(int(a,2))