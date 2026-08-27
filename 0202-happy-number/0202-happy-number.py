class Solution:
    def isHappy(self, n: int) -> bool:
        # to check if Number n is Happy
        # positive number replace numebr by sum of square of digits
        # repeat process till number == 1
        # iF ends with 1 then Happy so return True else return False
        
        #Solution : Should use Hashset 
        seen=set()
        while n!=1:
            #if we have already seen the value in the set we are in an infinite cycle
            if n in seen:
                return False
            seen.add(n)

            #calculate the sum of squares
            new_num=0
            while n>0:
                digit = n%10
                new_num+=digit*digit
                n=n//10
            n=new_num
        return True