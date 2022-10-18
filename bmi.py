#  Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#  Don't change the code above 👆

#calculated bmi
int_height = float(height)
int_weight = int(weight)


bmi = round(int_weight / int_height ** 2)

#added else/if statements
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")