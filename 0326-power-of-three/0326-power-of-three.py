class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        count=0
        if n<=0:
            return False
        while n>0:
            digit=n%3
            if (digit==1):
                count+=1
                if count>1:
                    return False
            if (digit==2):
                return False
            n//=3
        return count==1
        '''
        if n<=0:
            return False
        while n%3==0:
                n//=3
        return n==1