# http://www.lintcode.com/zh-cn/problem/number-of-islands/#

grid = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        
        self.grid = grid
        self.yy, self.xx = len(grid), len(grid[0])
        self.island_list = []
        
        for y in range(self.yy):
            for x in range(self.xx):
                cell = grid[y][x]
                if cell == 1:
                    pos = (y, x)
                    
                    if self.island_visited(pos):
                        continue
                    
                    island = set()
                    self.visit_island(pos, island)
                    self.island_list.append(island)
        
        return len(self.island_list)
    
    def island_visited(self, pos):
        for row in self.island_list:
            if pos in row:
                return True
        return False
    
    def visit_island(self, pos, island):
        island.add(pos)
        
        node = self.top(pos, island)
        if node:
            self.visit_island(node, island)
        
        node = self.left(pos, island)
        if node:
            self.visit_island(node, island)
            
        node = self.right(pos, island)
        if node:
            self.visit_island(node, island)
        
        node = self.bottom(pos, island)
        if node:
            self.visit_island(node, island)
    
    def top(self, pos, island):
        y, x = pos
        y -= 1
        if y < 0 or (y, x) in island or self.grid[y][x] == 0:
            return None
        return (y, x)
    
    def left(self, pos, island):
        y, x = pos
        x -= 1
        if x < 0 or (y, x) in island or self.grid[y][x] == 0:
            return None
        return (y, x)
    
    def right(self, pos, island):
        y, x = pos
        x += 1
        if x > self.xx - 1 or (y, x) in island or self.grid[y][x] == 0:
            return None
        return (y, x)
    
    def bottom(self, pos, island):
        y, x = pos
        y += 1
        if y > self.yy - 1 or (y, x) in island or self.grid[y][x] == 0:
            return None
        return (y, x)


solution = Solution()
result = solution.numIslands(grid)
print(result)

