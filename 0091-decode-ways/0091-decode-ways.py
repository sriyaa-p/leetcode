class Solution:
    def numDecodings(self, s: str) -> int:
        #using dynamic programming
        
        # Step-1 Find the Length of the string:
        n=len(s)
        #Step-2 Check if first index is 0
        if s[0]=='0':
            return 0
        #Step-3 Initialise dp
        dp=[0]*(n+1)
        #Number of ways to do nothing
        dp[0]=1
        #Number of ways to do 1
        dp[1]=1
        #Step-4 run the decoding loop
        for i in range(2,n+1):
            if s[i-1]!='0':
                dp[i]+=dp[i-1] #number of ways to decode current digit + the prev digit
            two_digits=int(s[i-2:i])
            if 10 <=two_digits<= 26:
                dp[i]+=dp[i-2]
        #return the number of ways it can be recieved        
        return dp[n]