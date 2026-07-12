a = int(input("Enter a: "))
b = int(input("Enter b: "))
operator = input("Enter the operator: ")
if operator == +:
  print("sum:",a+b)
elif operator == -:
  print("difference:",a-b)
elif operator == *:
  print("mult:",a*b)
elif operator == /:
  print("div:",a/b)
elif operator == //:
  print("quotient:",a//b)
elif operator == **:
  print("power:",a**b)
elif operator == %:
  print("reminder:",a%b)
else:
  print("Invalid operator")
