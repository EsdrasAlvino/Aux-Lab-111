horas = int(input("introduza una hora"))
if horas > 24:
    print("Número no válido")
minutos = int(input("introduzca un minuto"))
if minutos > 59:
    print("Número no válido")
segundos = int(input("introduzca un segundo"))
if segundos > 59:
    print("Número no válido")
    print("Resultado erróneo")
print ("Tiempo:", horas, "h,", minutos, "m,", segundos, "s")
print ("Tiempo:", horas, "h,", minutos, "m,", segundos +1, "s")