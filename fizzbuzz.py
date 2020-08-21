# prints fizz on multiples of 3
# prints buzz on multiples of 5
# prints fizz buzz on multiples of 3 and 5

def is_multiple(i,n):
	if i % n == 0:
		return True
	else:
		return False

checks = { 3: "fizz", 5: "buzz"}

for i in range(1,101,1):
	message = ""
	for key in checks:
		if (is_multiple(i, key)):
			message = message + checks[key]
	print(message or i)







	# binary = is_multiple(i,3) + is_multiple(i,5)
	# decimal = int(binary, 2)
	# if decimal == 3:
	# 	print("fizzbuzz")
	# elif decimal == 2:
	# 	print("fizz")
	# elif decimal == 1:
	# 	print("buzz")
	# else:
	# 	print(i)

	
