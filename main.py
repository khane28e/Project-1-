weight = float(input("enter the weight:"))
unit = (input("(K or L):"))

if unit == "K":
  weight = weight * 2.205
  unit = "Lbs"
  print(f"your weight is {round(weight)} {unit}")

elif unit == "L":
  weight = weight * 2.205
  unit = "kgs"
  print(f"your weight is {round(weight)} {unit}")

else:
  unit == ""
  print(f"{unit} invalid Unit!")