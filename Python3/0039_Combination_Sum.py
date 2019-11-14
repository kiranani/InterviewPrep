class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, n = [], len(candidates)
        def backtrack(i, total, acc):
            if total == target:
                ans.append(acc)
            elif total < target:
                for j in range(i, n):
                    if total + candidates[j] > target:
                        break
                    backtrack(j, total + candidates[j], acc + [candidates[j]])
        backtrack(0, 0, [])
        return ans
        
