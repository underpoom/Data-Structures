import timeit

start = timeit.default_timer()
from itertools import permutations

N = 8		 
numSol = 0  			

b = N*[-1]  			
colFree = N*[1] 			
upFree = (2*N - 1)*[1] 		
downFree = (2*N - 1)*[1]    		

def printBoard(b):
    print(b)

def putQueen(r, b, colFree, upFree, downFree):
    global N
    global numSol
    for c in range(N): 
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: 
            b[r] = c   

            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 

            if r == N-1:      
              
                numSol += 1
            else:
                putQueen(r+1, b, colFree, upFree, downFree) 
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 
           
putQueen(0, b, colFree, upFree, downFree)  

stop = timeit.default_timer()

print("recursive, n =",N)
print(str(numSol) + " Solutions")
print('Time:', round(stop - start,6),"Sec")  #Timer



