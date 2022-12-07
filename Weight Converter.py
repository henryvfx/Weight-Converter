weight = input("Enter your weight: ")
unit = input("(K)gs or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("Your weight in Lbs is: " + str(converted))
else:
    converted = float(weight) * 0.45
    print("Your weight in Kgs is: " + str(converted))
