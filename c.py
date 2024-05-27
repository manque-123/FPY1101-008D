asientos = []
num_asiento = 1
for i in range(10):
    numero=[]
    for j in range(4):
        numero.append(num_asiento)
        num_asiento+=1
    asientos.append(numero)
for i in asientos:
    print( "[", end="\t"  )
    for j in i:
        print("[",j, end="]\t")
    print("]")
    