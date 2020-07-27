def convertF(fTemp):
	c = (fTemp - 32) * (5 / 9)
	print(fTemp, "Fahrenheit is equal to: %.3f" % c, "Celsius.")
	
	fTemp = float(input("Enter Fahrenheit temp to convert: "))
	
	convertF(fTemp)