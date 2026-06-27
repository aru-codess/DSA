class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        
        if is_neg: x = abs(x)

        res = 0

        while x:
            rem = x % 10
            res = ((res * 10) + rem)
            x //= 10
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return -res if is_neg else res 