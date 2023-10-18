myTable = [5, 3, 4, 7, 1]
print(myTable)

stokage = 0
plusgrand = myTable[0]
suivante = 0
for i in range (len(myTable)):
    plusgrand = myTable[i]
    for n in range(i, len(myTable)):
        if myTable[n]< plusgrand:
            suivante = i + 1
            plusgrand = myTable[n]
            stokage = myTable[n]
            myTable[n] = myTable[suivante] 
            myTable[suivante] = stokage





print(myTable)