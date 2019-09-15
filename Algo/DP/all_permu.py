class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        import copy
        def dfs(candidates, path, res, visited):
            if len(path) == len(candidates):
                x = copy.copy(path)
                res.append(x)
                return 
            for i in range(0, len(candidates)):
                if not visited[i]:
                    if i > 0 and candidates[i] == candidates[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True
                    dfs(candidates, path+[candidates[i]], res, visited)
                    visited[i] = False
        res = []
        A.sort()
        visited = [False]*len(A)
        dfs(A, [], res, visited)
        return res
