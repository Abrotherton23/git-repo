
weight = int(input("How much do you weigh?: "))
kind = input("(K)Kilo (L)LB: ")

if kind.upper() == "K":
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kgs: " + str(converted))


