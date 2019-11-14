class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, n = [], len(candidates)
        def backtrack(i, total, acc):
            if total == target:
                ans.append(acc)
            elif total < target:
                for j in range(i, n):
                    if total + candidates[j] > target:
                        break
                    elif j > i and candidates[j] == candidates[j - 1]:
                        continue
                    backtrack(j + 1, total + candidates[j], acc + [candidates[j]])
        backtrack(0, 0, [])
        return ans
        
