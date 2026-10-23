num = int(input("Enter a number:  "))
original = num
sum = 0
if num>=1:
	while num>0:
		digit = num%10
		factorial = 1
		for i in range(1,digit+1):
			factorial*=i
		sum+=factorial
		num = num//10
if original>=1 and original == sum:
	print("Strong number")
else:
	print("Not a Strong number")