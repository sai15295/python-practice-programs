num = int(input("Enter a number:  "))
original = num
sum = 0
while num>0:
	digit = num%10
	sum+=digit**3
	num = num//10
if sum == original:
	print("An Armstrong number")
else:
	print("Not an Armstrong number")