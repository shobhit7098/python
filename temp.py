unit= input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp= float(input("Enter the tempererature : "))
if unit == "C":
       temp =round( (9*temp) / 5 + 32,1)
       print("The temperature in Fahrenheit is :{temp}°F")
elif unit == "F":
       temp= round((temp - 32)* 5/9 , 1)
       print("The temperature in Celsius is :{temp}°C")
else:
       print("{unit} is invalid unit of measurement")