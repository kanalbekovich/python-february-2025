# tip=int(input("Enter tip percentage: "))

choice=int(input("""
Select your choice:
1 - 15%
2 - 18%
3 - 20%
4 - type number
"""))

if choice == 1:
    print("Standard")
elif choice == 2:
    print("Good")
elif choice == 3:
    print("Great")
elif choice == 4:
   tip=int(input("Enter tip percentage: "))
   if tip > 20:
     print("My hero")
   else: 
    print("Provide right percentage")
else: 
    print("Provide right percentage")

