class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        c = 1
        for i in range(len(digits)):
            c, digits[~i] = divmod(c + digits[~i], 10)
        if c:
            return [c] + digits
        else:
            return digits
