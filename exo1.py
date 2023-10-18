myTable = [1, 2 ,5 ,4, 7]
stokage = 0
print(myTable)

case1 = int(input("Choisir une case\n"))
case2 = int(input("Choisir une autre case\n"))         

stokage = myTable[case1]
myTable[case1] = myTable[case2] 
myTable[case2] = stokage

print(myTable)