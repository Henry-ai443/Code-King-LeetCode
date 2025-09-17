class Solution:
    def isPalindrome(self,num):
        if num < 0:
            return False
        
        return str(num) == str(num)[::-1]