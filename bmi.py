#  Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#  Don't change the code above 👆

#calculated bmi
int_height = float(height)
int_weight = int(weight)


bmi = round(int_weight / int_height ** 2)