class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        subset = []
        seen = set()

        def helper(start, total):
            if total == target:
                sol.append(subset.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicate choices at this level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since sorted, everything after this is too large
                if total + candidates[i] > target:
                    break

                subset.append(candidates[i])
                helper(i + 1, total + candidates[i])
                subset.pop()

        helper(0, 0)
        return sol
            

