heading = """ BMI Calculator\n
1. Weight in pounds, height in inches
2. Weight in kilograms, height in meters"""
print(heading)
choice = int(input("\nChoice: "))

if choice == 2:
    weightK = float(input("Weight in kilograms? : "))
    heightM = float(input("Height in meter? : "))
    BMI = round(weightK /(heightM**2),2)
    status = ""
    if BMI >= 30:
        status = "Obese"
    elif BMI <= 29 and BMI >= 25:
         status = "Overweight"
    elif BMI >= 18.5 and BMI <= 25:
         status ="Normal"
    else:
         status = "Underweight"
        
    print("\nResult...........................................................")
    print("Weight: ",weightK," Kilograms")
    print("Height: ",heightM," meters")
    print("BMI: ",BMI)
    print("Status: ",status)

elif choice == 1:
    weightP = float(input("Weight in pounds? : "))
    heightI = float(input("Height in inches? : "))
    BMI = weightP /(heightI **2)*703
    status = ""
    if BMI >= 30:
        status = "Obese"
    elif BMI >= 29 and BMI >= 25:
         status = "Overweight"
    elif BMI >= 18.5 and BMI <= 25:
         status ="Normal"
    else:
         status = "Underweight"
        
    print("Result...........................................................")
    print("Weight: ",weightP," pounds")
    print("Height: ",heightI," inches")
    print("BMI: ",BMI)
    print("Status: ",status)

else:
    print("Goodbye wrong Input!!")

    
          
