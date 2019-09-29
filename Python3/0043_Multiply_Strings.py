class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        n, num1, num2 = n1 + n2, [int(x) for x in num1], [int(x) for x in num2]
        q = [0] * n
        for i in range(n1):
            c = 0
            for j in range(n2):
                c, q[~(i + j)] = divmod(c + q[~(i + j)] + num1[~i] * num2[~j], 10)
            q[~(i + j + 1)] = c
        i = 0
        while i < n - 1 and q[i] == 0:
            i += 1
        return "".join([str(x) for x in q[i:]])
        
