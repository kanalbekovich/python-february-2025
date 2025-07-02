years=int(input("Enter number of years: "))

choice=input("""
Select your choice:
1 - Days
2 - Weeks
3 - Hours
""")

if choice == "1":
    print(f"In {years} years there are {365*years} days")
elif choice == "2":
    print(f"In {years} years there are {52*years} weeks")
elif choice == "3":
    print(f"In {years} years there are {365*24*years} hours")
else:
    print("Select a right choice")


    



