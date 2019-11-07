from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for path in paths:
            path = path.split()
            for f in path[1:]:
                tokens = f.split("(")
                h[tokens[1][:-1]].append(path[0] + "/" + tokens[0])
        return [v for k, v in h.items() if len(v) > 1]
