def BMI():
    print("Welcome to the BMI Calculator")
    weight = input("Enter Your Weight: ")
    height = input("Enter Your Height: ")
    bmi = round(int(weight) / float(height) ** 2, 2)
    print("Your BMI is: ", bmi)
BMI()
