print(f"Welcome to the BMI calculator")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / (height ** 2))
print(bmi)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, are underweight")
elif bmi < 25: 
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
else: 
    print("You are obese")