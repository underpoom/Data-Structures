from itertools import permutations
import timeit
N = 8

start = timeit.default_timer()
from itertools import permutations

def print_table():
    for row in range(N):
        print(table[row])

def put_queen(x,y):
    if not table[y][x]:
        for m in range(N):
            table[y][m] = table[m][x] = 1
            table[y][x] = 2
            if y+m <= N-1 and x+m <= N-1:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= N-1:
                table[y-m][x+m] = 1
            if y+m <= N-1 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False

table = [[0]*N for _ in range(N)]    
perms = permutations([i for i in range(N)])
num_comb = 0

for perm in perms:
    for i in range(N):
        if put_queen(perm[i], i) == False:
            break
    else:
        print_table()
        num_comb += 1
        print("solution" + str(num_comb) +'\n')
                            
    table = [[0] * N for _ in range(N)]

stop = timeit.default_timer()
print('Time: ', stop - start)  #Timer