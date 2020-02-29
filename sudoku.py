import numpy as np
import sys
num_soluciones = 0
grid=[]
def ispossible (y,x,n):
    global grid
    for i in range (0,9):
        if grid [y][i]==n:
            return False
    for i in range (0,9):
        if grid [i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range (0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve ():
    global grid
    global num_soluciones
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if ispossible(y,x,n):
                        grid [y][x]=n
                        solve()
                        grid [y][x]=0
                return
    num_soluciones= num_soluciones+1
    print(np.matrix(grid))
def main():
    if len(sys.argv)==2:
        input = open(sys.argv[1], "r")
    else:
        print("Introduce el nombre del archivo de entrada")
        return
    for i in range(9):
        grid.append([])
        new = input.readline()
        newsep = new[:-1].split(" ")
        for j in range(9):
            grid[i].append(int(newsep[j]))
    solve()
    print ("No hay mas soluciones, ",num_soluciones," soluciones")



main()
