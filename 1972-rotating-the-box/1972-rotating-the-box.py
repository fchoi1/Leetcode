class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        cols = len(box[0])
        rows = len(box)
        for y in range(rows):
            slow = count = 0
            for x in range(cols):
                if box[y][x] == '*':
                    while slow <=x and count > 0:
                        box[y][slow] = '#'
                        slow += 1
                        count -= 1
                    slow += 1
                elif box[y][x] == '#':
                    count += 1
                    box[y][x] = '.'
                else:
                    slow += 1
            while slow <= x and count > 0:
                box[y][slow] = '#'
                slow += 1
                count -= 1
        print(box)
        return [list(reversed(col)) for col in zip(*box)]

        