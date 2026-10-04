num = int(input("Enter a number:  "))
sum = 0
while num>0:
	digit = num%10
	num = num//10
	if digit%2 == 0:
		sum+=digit
print("Sum of even numbers: ",sum)
	