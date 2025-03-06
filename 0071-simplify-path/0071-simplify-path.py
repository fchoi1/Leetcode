class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        def getNextFolder(index):

            while index < len(path) and path[index] == '/':  # index = 5 -> 7
                index += 1

            name = ''
            while index < len(path) and path[index] != '/': # index = 1 -> 5 | index = 7 -> 10
                name += path[index]
                index += 1

            return (name, index) # home, 5 | foo, 10



        index = 0
        while index < len(path): # 0

            char = path[index] # 
            if char == '/':
                nextFolder, index = getNextFolder(index) # home, 5 | foo, 10

                if not nextFolder: # reach the end
                    break

                if nextFolder == '.':
                    continue

                if nextFolder == '..' and stack:
                    stack.pop()
                elif nextFolder != '..':
                    stack.append(nextFolder) # [home, foo]
            else:
                print('err')


        return "/" + "/".join(stack)
        