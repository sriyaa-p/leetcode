class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing_zeros=0
        while n>0:
            n//=5
            trailing_zeros+=n
        return trailing_zeros