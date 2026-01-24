class Solution(object):
    def isPalindrome(self, x):
        c=str(x)
        b=''
        c=c
        if x<0:
            return False  
        if int(c[::-1])==x:
            return True
        else: 
            return False
        