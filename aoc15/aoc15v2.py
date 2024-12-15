class Moveable:
    def __init__(self, i, j, size):
        self.pos = {(i,j+k) for k in range(size)}
        self.stuck = False
        self.movehist = {}
    
    def shift(self, di, dj):
        return {(i+di, j+dj) for i,j in self.pos}
    
    def covers(self, pos):
        return not pos.isdisjoint(self.pos)
    
    def checkstuck(self, walls):
        if self.stuck:
            return True
        mu = [pos in walls for pos in self.shift(-1,0)]
        md = [pos in walls for pos in self.shift(+1,0)]
        mr = max(self.shift(0,+1)) in walls
        ml = min(self.shift(0,-1)) in walls
        self.stuck = ((any(mu) and any(md)) or all(mu) or all(md)) and (ml or mr)
        return self.stuck

    def boxestomove(self, t, di, dj, boxes, walls):
        if t in self.movehist:
            return self.movehist[t]
        if self.stuck:
            self.movehist[t] = set()
        elif not self.shift(di, dj).isdisjoint(walls):
            self.movehist[t] = set()
        else:
            self.movehist[t] = {self}
            for i,j in self.shift(di,dj):
                if (i,j) in boxes:
                    tomove = boxes[(i,j)].boxestomove(t, di, dj, boxes, walls)
                    if tomove:
                        self.movehist[t].update(tomove)
                    else:
                        self.movehist[t] = set()
                        break
        return self.movehist[t]
    
    def move(self, di, dj):
        self.pos = self.shift(di,dj)

    def gps(self):
        i,j = min(self.pos)
        return 100*i + j

with open('input.txt') as file:
    block1, block2 = file.read().split('\n\n')

dirs = {'>':(0,1), 'v':(1,0), '<':(0,-1),'^':(-1,0)}
moves = [dirs[c] for c in ''.join(block2.split('\n'))]

boxes = {1:{}, 2:{}}
walls = {1:set(), 2:set()}
robot = {}
for i, line in enumerate(block1.split('\n')):
    for j, c in enumerate(line):
        if c == '#':
            walls[1].add((i,j))
            walls[2].add((i,2*j))
            walls[2].add((i,2*j+1))
        if c == 'O':
            boxes[1][(i,j)] = Moveable(i,j,1)
            box = Moveable(i,2*j,2)
            boxes[2][(i,2*j)] = box
            boxes[2][(i,2*j+1)] = box
        if c == '@':
            robot[1] = Moveable(i,j,1)
            robot[2] = Moveable(i,2*j,1)

for p in [1,2]:
    for t, (di, dj) in enumerate(moves):
        #for box in boxes[p]:
        #    if box.checkstuck(walls[p]):
        #        walls[p].update(box.pos)
        tomove = robot[p].boxestomove(t, di, dj, boxes[p], walls[p])
        if tomove:
            for box in tomove - {robot[p]}:
                for i,j in box.pos:
                    boxes[p].__delitem__((i,j))
                box.move(di,dj)
            for box in tomove - {robot[p]}:
                for i,j in box.pos:
                    boxes[p][(i,j)] = box
            robot[p].move(di,dj)
    print(f'Part {p}:', sum(box.gps() for box in boxes[p].values())//p)

    n, m = max(walls[p])
    grid = [['.' for j in range(m+1)] for i in range(n+1)]
    for i,j in walls[p]:
        grid[i][j] = '#'
    for box in boxes[p].values():
        c = 'S' if box.stuck else 'O'
        for i,j in box.pos:
            grid[i][j] = c
    print('\n'.join(''.join(line) for line in grid))