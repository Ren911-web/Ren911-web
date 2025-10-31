'''
Condicionales IF
'''

dato=int(input("ingrese un numero:"))

if dato>0 and dato<=100:
    print("El numero es positivo")
elif dato<0:
    print("El numero es negativo")
elif dato> 100:
    print("El numero es mayor a 100")    
else:
    print("Vacio")