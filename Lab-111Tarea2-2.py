a = int(input("Introduce un valor para a:"))
b = int(input("Introduce un valor para b:"))
c = int(input("Introduce un valor para c:"))
print("Calculando el Discriminante...")
print("El Discriminante es:")
D = b**2 - 4*a*c
print(D)
if D<0:
    print("Por lo tanto...NO existen soluciones reales")
