s = input('* Minesweeper *'+'\nEnter input(5x5) : ').split(',')
print('\n')
for i in range(5):
    s[i]=s[i].split()
    print(s[i])
print('\n')
id = [ [-1,-1],[-1,0],[-1,+1],[0,-1],[0,+1],[+1,-1],[+1,0],[+1,+1]]
for i in range(5):
    for j in range(5):
        if s[i][j]=='-':
            s[i][j]=0
            for k in range(8):           
                if i-1>=0 and j-1>=0 and i+1<=4 and j+1<=4 and s[i+id[k][0]][j+id[k][1]]=='#':
                    s[i][j]+=1
        s[i][j]=str(s[i][j])
print(*s,sep='\n')