class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        output = 0

        while num > 0:
            rem = num % 10
            output = output * 10 + rem
            num //= 10

        return output == x
            
