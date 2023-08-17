convert = 0.45
weight = int(input("Enter the Weight:"))
kilo_or_lbs = input("weight is in kilograms(K) or lbs(L):")
if kilo_or_lbs.upper() == 'K':
    weight = weight / convert
elif kilo_or_lbs.upper() == 'L':
    weight = weight * convert
else:
    print("Enter Valid value")
print("Converted value:",weight)
