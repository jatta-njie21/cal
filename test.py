def addition():
	pass

def subtraction():
	pass

def multiplication():
	pass

def division():
	pass

def modulos():
	pass

def inputs():
	
	num1 = float(input("NUM1 = "))
	num2 = float(input("NUM1 = "))
	operand = input("OPERAND =  ")

	if operand == "+" or "plus" or "p" or "P" or "PLUS" or "Plus":
		addition()

	elif operand == "-" or "minus" or "m" or "M" or "MINUS" or "Minus":
 		subtraction()

	elif operand ==  "*" or "times" or "t" or "T" or "TIMES" or "Times":
		multiplication()

	elif operand == "/" or "div" or "d" or "D" or "DIVIDE" or "Divide":
		division()

	elif operand == "%" or "mod" or "md" or "MD" or "MOD" or "Mod":
		modulos()

	else:
		print("INVALID OPERAND!!!!!")

while True:
	inputs()