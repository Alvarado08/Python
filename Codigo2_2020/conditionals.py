edad1 = 5
edad2 = 5
edad3 = 6
if edad1 > edad2:
    print("Yo mando!!")
elif edad1==edad2:
    print("Nadie manda")
else:
    print("Ella manda!!")

if edad1 < edad3 and edad3 > edad2:
    print("Correcto")

result = edad1 if edad2 < edad3 else edad3
print(result)
