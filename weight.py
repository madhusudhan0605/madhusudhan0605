convert = 0.45
weight = int(input("Enter the Weight "))
kilo_or_lbs = input("weight is in kilo grams or lbs ")
if kilo_or_lbs.upper() == 'K':
    weight = weight / convert
elif kilo_or_lbs.upper() == 'L':
    weight = weight * convert
print(weight)
