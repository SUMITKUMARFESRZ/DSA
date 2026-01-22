class Solution(object):
    def reverse(self, x):
        a = str(x)
        if x < 0:
            b = '-' + a[:0:-1]
        else:
            b = a[::-1]
        c=int(b) 
        if int(b) < (-2**31) or int(b) > (2**31 - 1):
            return 0
        else:
            return int(b)