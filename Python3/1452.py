class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        if not favoriteCompanies:
            return 0
        favComps = [set(i) for i in favoriteCompanies]
        sInd = sorted(range(len(favComps)), key=lambda x: -len(favComps[x]))
        ans = {sInd[0]}
        for i in sInd[1:]:
            s, isSubset, inValid = favComps[i], False, set()
            for j in ans:
                if len(s) == len(s & favComps[j]):
                    isSubset = True
                    if len(s) == len(favComps[j]):
                        inValid.add(j)
            if not isSubset:
                ans.add(i)
            ans -= inValid
        return sorted(ans)
        
