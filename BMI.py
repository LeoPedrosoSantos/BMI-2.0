print("***BMI Calculator***\n")

Height = input("What is your Height?\n")
Weight = input("What is your Weight?\n")

Height_int = float(Height)
Weight_int = int(Weight)

BMI = Weight_int / (Height_int ** 2)

print(f"Your BMI is {round(BMI ,2)}\n")

if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are in normal weight")
elif BMI < 30:
    print("You are slightly overweight")
elif BMI < 35:
    print("You are obese")
else:
    print("You are clinically obese")

print(input("\nClick ENTER to close the window"))