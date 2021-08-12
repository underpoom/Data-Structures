print('*** Minesweeper ***')
s = input('Enter input(5x5) : ').split(',')

print('\n')

for i in range(5):
    s[i] = s[i].split()
    print(s[i])

print('\n')
for i in range(5):
    for j in range(5):
        if(s[i][j] == '-'):
            s[i][j] = 0
            if(i-1 >= 0 and s[i-1][j] == '#'): 
                s[i][j] += 1
            if(i-1 >= 0 and j+1 <= 4 and s[i-1][j+1] == '#'): 
                s[i][j] += 1
            if(j+1 <= 4 and s[i][j+1] == '#'):
                s[i][j] += 1
            if(j+1 <= 4 and i+1 <= 4 and s[i+1][j+1] == '#'):
                s[i][j] += 1
            if(i+1 <= 4 and s[i+1][j] == '#'):
                s[i][j] += 1
            if(i+1 <= 4 and j-1 >= 0 and s[i+1][j-1] == '#'):
                s[i][j] += 1
            if(j-1 >= 0 and s[i][j-1] == '#'):
                s[i][j] += 1  
            if(i-1 >= 0 and j-1 >= 0 and s[i-1][j-1] == '#'):
                s[i][j] += 1  
        s[i][j] = str(s[i][j])          

    
print(*s,sep=('\n'))