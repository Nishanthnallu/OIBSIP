weight = float(input("Enter your weight in kg = "))
height = float(input("Enter your height in meters ="))

if weight<=0 or height <= 0:
    print("Enter a valid weight or height")

BMI = weight / (height**2)

print(f"BMI = {BMI:.2f}" )

if BMI < 18.5:
    print("You are underweight")

elif 18.5<= BMI <= 24.9:
    print("You are healthy")

elif 25<= BMI <=29.9:
    print("You are weight")

else:
    print("You are Obese")

    












