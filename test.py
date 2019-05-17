weight = 90
height = 1.80
bmi = weight / (height ** 2)

bmi = 18
print(bmi)

if bmi > 25:
    print("over")
elif bmi < 18:
    print("under")
else:
    print("normal")
