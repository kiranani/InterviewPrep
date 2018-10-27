class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def dfs(email):
            a = [email]
            visited.add(email)
            for e in graph[email]:
                #print(email, visited)
                if e not in visited:
                    a.extend(dfs(e))
            #print(a)
            return set(a)

        name_hash, graph = {}, collections.defaultdict(set)
        for account in accounts:
            #print(graph)
            for i, email in enumerate(account[1:]):
                name_hash[email] = account[0]
                for j in range(i + 1, len(account) - 1):
                    graph[email].add(account[j + 1])
                    graph[account[j + 1]].add(email)
                if len(account) == 2:
                    graph[email] = set()

        visited, ans = set(), []
        for email in graph:
            if email not in visited:
                ans.append(dfs(email))
        ans = [sorted(x) for x in ans]
        return [[name_hash[x[0]]] + x for x in ans]
