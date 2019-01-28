with open('input2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
    b = lines[0]
    b = int(b[:-1])
    p = lines[1]
    p = int(p[:-1])
    L = lines[2]
    L = int(L[:-1])
    top =3
    Llines = lines[top:top+L]
    for index,value in enumerate(Llines):
        Llines[index] = Llines[index][:-1]
    top += L
    S = lines[top]
    S = int(S[:-1])
    top+=1
    Slines = lines[top:top+S]
    for index,value in enumerate(Slines):
        Slines[index] = Slines[index][:-1]

    top+=S
    A = lines[top]
    A = int(A[:-1])
    top+=1
    Alines = lines[top:]
    for index,value in enumerate(Alines):
        Alines[index] = Alines[index][:-1]

    LAHSA = []
    SPLA = []
    together = 0
    Both = []
    for index, value in enumerate(Alines):
        together = 0
        if value[:5] not in Llines and value[:5] not in Slines:
            if value[5]=='F' and int(value[6:9])>17 and value[9] =='N' :
                LAHSA.append(value)
                together +=1
        if value[:5] not in Slines and value[:5] not in Llines:
            if value[10] =='N' and value[11] == 'Y' and value[12] == 'Y':
                SPLA.append(value)
                together+=1
        if together == 2:
            Both.append(value)
    weight = 0
    newweight = 0
    select = ''
    if len(Both)>0:
        for index, value in enumerate(Both):
            newweight = int(value[13])+int(value[14])+int(value[15])+int(value[16])+int(value[17])+int(value[18])+int(value[19])
            if newweight>weight:
                weight = newweight
                select = value[:5]
    else:
        for index, value in enumerate(SPLA):
            newweight = int(value[13])+int(value[14])+int(value[15])+int(value[16])+int(value[17])+int(value[18])+int(value[19])
            if newweight>weight:
                weight = newweight
                select = value[:5]
with open('output2.txt','w')as k:
    k.write(select)




