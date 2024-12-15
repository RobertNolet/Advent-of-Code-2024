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

    def canmove(self, t, di, dj, boxes, walls):
        if t in self.movehist:
            return self.movehist[t]
        if self.stuck:
            self.movehist[t] = False
        elif not self.shift(di, dj).isdisjoint(walls):
            self.movehist[t] = False
        else:
            self.movehist[t] = True
            for box in boxes:
                if (box != self and
                    box.covers(self.shift(di,dj)) and 
                    not box.canmove(t, di, dj, boxes, walls)):
                    self.movehist[t] = False
                    break                
        return self.movehist[t]
    
    def move(self, di, dj, boxes, walls):
        for box in boxes:
            if box != self and box.covers(self.shift(di,dj)):
                box.move(di, dj, boxes, walls)
        self.pos = self.shift(di,dj)

    def gps(self):
        i,j = min(self.pos)
        return 100*i + j

with open('input.txt') as file:
    block1, block2 = file.read().split('\n\n')

dirs = {'>':(0,1), 'v':(1,0), '<':(0,-1),'^':(-1,0)}
moves = [dirs[c] for c in ''.join(block2.split('\n'))]

boxes = {1:set(), 2:set()}
walls = {1:set(), 2:set()}
robot = {}
for i, line in enumerate(block1.split('\n')):
    for j, c in enumerate(line):
        if c == '#':
            walls[1].add((i,j))
            walls[2].add((i,2*j))
            walls[2].add((i,2*j+1))
        if c == 'O':
            boxes[1].add(Moveable(i,j,1))
            boxes[2].add(Moveable(i,2*j,2))
        if c == '@':
            robot[1] = Moveable(i,j,1)
            robot[2] = Moveable(i,2*j,1)

for p in [1,2]:
    for t, (di, dj) in enumerate(moves):
        #for box in boxes[p]:
        #    if box.checkstuck(walls[p]):
        #        walls[p].update(box.pos)
        if robot[p].canmove(t, di, dj, boxes[p], walls[p]):
            robot[p].move(di, dj, boxes[p], walls[p])
    print(f'Part {p}:', sum(box.gps() for box in boxes[p]))

    n, m = max(walls[p])
    grid = [['.' for j in range(m+1)] for i in range(n+1)]
    for i,j in walls[p]:
        grid[i][j] = '#'
    for box in boxes[p]:
        c = 'S' if box.stuck else 'O'
        for i,j in box.pos:
            grid[i][j] = c
    print('\n'.join(''.join(line) for line in grid))