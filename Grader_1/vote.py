print('* Election *')
n,p,vote = int(input('Enter a number of voter(s) : ')),[int(e) for e in input().split(' ')],[]
for i in p: 
    if(i > 0 and i <=20) : vote.append(int(i)) 
if len(vote)<1 : print('* No Candidate Wins *')
elif len(vote)>0 : print((max(vote,key=vote.count)))

   