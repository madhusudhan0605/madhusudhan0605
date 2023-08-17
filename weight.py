def weight_converter(convert,weight):
    kilo_or_lbs = input("weight is in kilograms(K) or lbs(L):")
    if kilo_or_lbs.upper() == 'K':
        weight = weight / convert
        print("Converted value:",weight)
    elif kilo_or_lbs.upper() == 'L':
        weight = weight * convert
        print("Converted value:",weight)
    else:
        print("Enter Valid value!!!")
        weight_converter(convert,weight)

convert = 0.45
weight = int(input("Enter the Weight:"))
weight_converter(convert,weight)

