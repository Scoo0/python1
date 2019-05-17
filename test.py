weight =float(input("enter kg:"))
height = float(input("enter your height:"))
bmi = weight / (height ** 2)

print(bmi)

if bmi > 25:
    print("ezafe kari dari dadash")
elif bmi < 18:
    print("bokhor namiri")
else:
    print("jon baba")
