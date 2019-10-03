class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = collections.defaultdict(int)
        for payer, payee, amount in transactions:
            balances[payer] += amount
            balances[payee] -= amount
        t, debts = 0, collections.Counter(balances.values())
        del debts[0]
        unsettled = []
        for d in debts:
            if debts[d] and debts[-d]:
                settle = min(debts[d], debts[-d])
                t += settle
                debts[d] -= settle
                debts[-d] -= settle
            unsettled.extend([d] * debts[d])
        n = len(unsettled)
        def dfs(i):
            while i < n and unsettled[i] == 0:
                i += 1
            if i == n:
                return 0
            m = float("inf")
            for j in range(i + 1, n):
                if unsettled[i] * unsettled[j] < 0:
                    unsettled[j] += unsettled[i]
                    m = min(m, 1 + dfs(i + 1))
                    unsettled[j] -= unsettled[i]
            return m
        return dfs(0) + t
        
