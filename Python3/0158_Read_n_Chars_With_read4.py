"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.i4 = 0
        self.buf4 = [""] * 4
        self.n4 = read4(self.buf4)
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n == 0:
            return 0
        i = 0
        while self.i4 < self.n4 and n:
            if n < self.n4 - self.i4:
                buf[i:i + n] = self.buf4[self.i4:self.i4 + n]
                n, i, self.i4 = 0, i + n, self.i4 + n
            else:
                buf[i:i + self.n4 - self.i4] = self.buf4[self.i4:self.n4]
                n, i = n - self.n4 + self.i4, i + self.n4 - self.i4
                self.i4, self.n4 = 0, read4(self.buf4)
        return i
                
            
        
