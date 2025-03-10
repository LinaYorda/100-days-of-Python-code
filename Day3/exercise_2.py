"""
Exercise 2 - BMI 2.0

Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

Example Input
weight = 85
height = 1.75
Example Output
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.

"""


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(float(weight / (height ** 2)))

if weight / (height * height) < 18.5:
    print(f"Your BMI is {BMI}, you are underweight!")

elif weight / (height * height) < 25:
    print(f"Your BMI is {BMI}, you have a normal weight!")

elif weight / (height * height) < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight!")

elif weight / (height * height) < 35:
    print(f"Your BMI is {BMI}, you are obese")

else:
    print(f"Your BMI is {BMI}, you are clinically obese!")




