class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        h, MOD = {(1, x): 1 for x in range(1, f + 1)}, 10 ** 9 + 7
        def backtrack(i, rem):
            if (i, rem) in h:
                return h[i, rem]
            elif i > 1 and rem > 0:
                t = 0
                for n in range(1, f + 1):
                    t += backtrack(i - 1, rem - n)
                h[i, rem] = t % MOD
                return h[i, rem]
            else:
                return 0
        return backtrack(d, target)
                
        
        
