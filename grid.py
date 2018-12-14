for i in range(0, 100):
    print("\n")
grid = [ ['__ '] * 8] * 8
for i in range (0, 8):
    for j in range(0, 8):
        print(grid[i][j], end = ' ')
    print(i+1)
    print("\n")