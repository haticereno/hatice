note =
float(input("Abschlussnote(0-100): "))
erfahrung =
int(input("Programmierefahrung (1-5): "))

if note > 90 or (erfahrung == 5 and note >= 70):
  print("einstellen")
elif note > 70 or erfahrung == 4:
   print("zum Gesprach einladen")
else:
  print("ablehnen")