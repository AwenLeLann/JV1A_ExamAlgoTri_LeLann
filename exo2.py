myTable = [5, 3, 4, 7, 1]
print(myTable)

stokage = 0
suivante = 0 

for i in range (len(myTable)):
    suivante = i+1
    if ( myTable[i]> myTable[suivante]):
       
        stokage = myTable[i]
        myTable[i] = myTable[suivante] 
        myTable[suivante] = stokage
    print(myTable)  

print(myTable)