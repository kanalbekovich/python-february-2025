while True:
    age=int(input("Enter your age: "))
    if age < 13:
        print("You are not allowed to pass")
    elif age >= 13 and age < 18:
        print("Call your legal guardian")
    else:
        print("Welcome")

