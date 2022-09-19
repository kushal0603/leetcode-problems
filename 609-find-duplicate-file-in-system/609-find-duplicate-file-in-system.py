class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        while paths:
            path_info = paths.pop()
            dir_, *fs = path_info.split()
            for f in fs:
                f_name, content = f.split('(')
                ans[content].append('/'.join((dir_, f_name)))

        return [val for val in ans.values() if len(val) > 1]