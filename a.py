mt = []
ls = []
for i in range(3):
    ls = [int(input(f"ingrese el digito [{i}][{j}]): ")) for j in range(4)]
    mt.append(ls)
for i in mt:
    print( "[", end=" " )
    for j in i:
        print(j, end= " ")
    print("]")
