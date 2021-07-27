def is_valid(grid,row,col,number):
    for x in range(9):
        if(grid[row][x]==number):
            return False
    for x in range(9):
        if(grid[x][col]==number):
            return False
    corner_row=row-row % 3
    corner_col=col-col % 3
    for x in range (3):
        for y in range(3):
            if (grid[corner_row+x][corner_col+y]==number):
                return False
def solve(grid,row,col):
    if col==9:
        if row==8:
            return True
        row=row+1
        col=0
    if(grid[row][col]>0):
        return solve(grid,row,col+1)
    for num in range(1,10):
        if is_valid(grid,row,col,num):
            grid[row][col]=num
            if solve(grid,row,col+1):
                return True
    grid[row][col]=0
    return False

    #####put your grid here
grid=[]
if solve(grid,0,0):
    for  i  in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()
else:
    print("No Solution...i am STUPID...GO SOLVE YOURSELVES")