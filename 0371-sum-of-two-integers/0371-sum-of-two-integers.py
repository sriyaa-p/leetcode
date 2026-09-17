class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff
        while (mask&b)>0:
            carry=(a&b)<<1 #(a&b) finds where carry occur and <<1 shifts 1 position left in case 1 occurs
            a=a^b
            b=carry
        return (mask&a) if b>0 else a