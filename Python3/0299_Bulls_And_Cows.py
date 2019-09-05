class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, m, h1, h2 = 0, 0, {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            h1[secret[i]] = 1 + h1.get(secret[i], 0)
            h2[guess[i]] = 1 + h2.get(guess[i], 0)
        m = 0
        for k in h1:
            if h2.get(k):
                m += min(h1[k], h2[k])
        return str(a) + "A" + str(m - a) + "B"
        
