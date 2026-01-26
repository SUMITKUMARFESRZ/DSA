class Solution(object):
    def smallestNumber(self, n):
        if (n&(n+1))==0:
            return n
        else:
            i=n
            while True:
                if(i&(i+1))==0:
                    break
                i+=1
        return i 