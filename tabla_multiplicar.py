# indicamos que inicie en 1, hasta la tabla del 12, incrementando de 1 en 1
for i in range(1, 13, 1):
    # indicamos que inicie en 1, hasta el valor que queramos multiplicar, incrementando de 1 en 1
    for j in range(1, 13, 1):
        print(f"{i}*{j} = {i*j}");
    print("\n"); # salto de linea

input("!!Presione enter para continuar...");