class Solution:
    def simplifyPath(self, path: str) -> str:
        my_dir = []
        path = path.split('/')

        for elem in path:
            if elem == '..' and my_dir:
                my_dir.pop()
            if elem not in ['.', '', '..']:
                my_dir.append(elem)

        return '/'+'/'.join(my_dir)
