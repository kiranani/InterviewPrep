class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        i, j, c = 0, len(s) - 1, 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)
        return True
        
