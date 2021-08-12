st,st1= [],[]
data = input('*** Fun with countdown ***' + '\nEnter List : ').split()
for i in range(len(data)):
    data[i] = int(data[i])  
    if (len(st)==0 or data[i-1]-1 == data[i] ):
        st.append(data[i])
    else:
        st.clear()
        st.append(data[i])
    if(len(st)!=0 and st[len(st)-1]==1):
        st1.append(st.copy())
        st.clear()

st1.append(st1.insert(0,st1.copy()))
st1.insert(0,len(st1)-2)
print(st1[0:2])