mon_num = input("Enter the month:  ")
if mon_num == '1' or mon_num == '3' or mon_num == '5' or mon_num == '7' or mon_num == '8' or mon_num == '10' or mon_num == '12':
	print("31 Days")
elif mon_num == '4' or mon_num == '6' or mon_num == '9'or mon_num == '11':
	print("30 Days")
elif mon_num == '2':
	print("28 or 29 days")