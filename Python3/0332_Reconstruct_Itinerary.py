class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for fro, to in tickets:
            heapq.heappush(graph[fro], to)
        ans = collections.deque()
        def dfs(fro):
            while graph[fro]:
                dfs(heapq.heappop(graph[fro]))
            ans.appendleft(fro)
        dfs("JFK")
        return ans
        
