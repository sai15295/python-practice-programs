age = int(input("Enter your age:  "))
if age<18:
	if age>=16:
		print("You are not eligible for voting")
		print("You are eligible to ride a gearless motor cycle with parent/guardian consent")
	else:
		print("You are not eligible for voting")
		print("You are not eligible for driving")
elif age>=18:
	if age<20:
		print("You are eligible for voting")
		print("You are eligible for driving motor cycles and cars with gears")
	elif age>=20:
		print("You are eligible for voting")
		print("You are eligible for driving commercial vehicles")
		
	

