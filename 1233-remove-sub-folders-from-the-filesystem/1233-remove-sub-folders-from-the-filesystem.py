class Trie:
    def __init__(self, name=None, end = False):
        self.name = name
        self.end = end
        self.children = {}

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # sort by number of /
        # Trie? 
        folder.sort(key=lambda x: x.count('/'))
        root = Trie()
        ans = []
        for f in folder:
            curr = root
            path = f.split('/')[1:]
            # print("PATH", path)
            for name in path:
                if name not in curr.children:
                    curr.children[name] = Trie(name)
             
                curr = curr.children[name]
                if curr.end:
                    break
            else:
                # print("append to ans", path, curr.name)
                curr.end = True
                ans.append(f)
        return ans
        