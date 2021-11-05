class dic:
    def __init__(self,s,w,l,d,sc,con):
        self.s = s
        self.tp = 3*w +0*l+ d
        self.gf = sc-con
    def __str__(self):
        return '[\''+self.s+'\'' + ', {\'points\': '+str(self.tp)+'}, {\'gd\': '+str(self.gf) + '}]'

def bubble_de(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j].tp < l[j+1].tp:
                l[j],l[j+1] = l[j+1],l[j]  
            elif l[j].tp == l[j+1].tp:
                if l[j].gf < l[j+1].gf:
                    l[j],l[j+1] = l[j+1],l[j]         
    return l

s = [str(e).split(',') for e in input('Enter Input : ').split('/')]
l = [ dic( e[0],int(e[1]),int(e[2]),int(e[3]),int(e[4]),int(e[5])) for e in s]
print('== results ==\n'+'\n'.join([str(e) for e in bubble_de(l)]))