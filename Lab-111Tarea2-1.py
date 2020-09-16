segundos = int(input("Introduce un valor de tiempo en segundos"))
minutos = segundos // 60
segundos_resto = segundos % 60
horas = minutos // 60
minutos_resto = minutos % 60
print ("Tiempo:", horas, "h,", minutos_resto, "m,", segundos_resto, "s")
if segundos ==3600:
    print("La Tarea se completó exitósamente")
elif segundos >3600:
    print("La Tarea se completó exitosamente")
    print("Le sobró tiempo")
else:
    print("Tarea no completada, por falta de tiempo")