print('Fun with countdown ')
data =  [int(e) for e in input('Enter list numbers : ').split()]
st,st1= ([],[])
for i in range(len(data)):
    st.append(data[i]) if (len(st)==0 or data[i-1]-1 == data[i] ) else (st.clear(),st.append(data[i]))
    (st1.append(st.copy()), st.clear()) if(len(st)!=0 and st[len(st)-1]==1) else ()
st1.append(st1.insert(0,st1.copy()))
st1.insert(0,len(st1)-2)
print(st1[0:2])