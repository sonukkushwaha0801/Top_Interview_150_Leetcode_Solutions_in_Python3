# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b,2)))[2:]
    
# Another way:
def decimalNumber(s):
        i=0
        sum=0
        for x in range(len(s)-1, -1, -1):
            twoNumber = 1<<i
            sum+= twoNumber*int(s[x])
            i+=1
        return sum
class Solution:
        def addBinary(self, a: str, b: str) -> str:
            if a=="0" and b=="0":
                return a

            result = decimalNumber(a)+decimalNumber(b)
            s=""
            while result>0:
                s+=str(result%2)
                result= result//2
            return s[::-1]


    
        