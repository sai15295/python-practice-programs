num = int(input("Enter a number:  "))
largest = 0
smallest = 10
while num>0:
	digit = num%10
	if digit>largest:
		largest = digit
	if digit<smallest:
		smallest = digit
	num = num//10
print(f"Largest digit: ",largest)
print(f"Smallest digit: ",smallest)