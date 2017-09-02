def celsius_to_fah(celsius):
	if temperature >= -273:
		fah=int(celsius)*9/5+32
		return fah
	else:
		return "not possible"




temperatures=[10,-20,-289,100]

for temperature in temperatures:
 		print(celsius_to_fah(temperature))