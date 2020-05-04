noms = ["\nFiona", "Shrek", "Burro\n"]
for nom in noms:
    print(nom)

for num in range(5):
    print(num)

for num2 in range(5,10):
    print(num2)

for num3 in range(10,20,2):
    print(num3)

cars = ["\nmustang", "ferrari", "camaro"]
for car in cars:
    print(car)
else:
    print("Done\n")

dogs = ["\nHusky", "Lab", "French\n"]
for dog in dogs:
    if dog == "Lab":
        continue
    print(dog)