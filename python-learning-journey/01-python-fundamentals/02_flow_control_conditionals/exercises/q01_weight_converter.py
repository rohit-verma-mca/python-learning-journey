# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("(K)g or (L)b: ").upper()

if unit == "K":
    converted_weight = weight * 2.20462
    print(f"Weight in pounds: {converted_weight:.2f} lb")
elif unit == "L":
    converted_weight = weight / 2.20462
    print(f"Weight in kilograms: {converted_weight:.2f} kg")
else:
    print("Invalid unit!")

