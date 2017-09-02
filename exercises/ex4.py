def celsius_to_fah(celsius):
	fah=int(celsius)*9/5+32
	return fah



temperatures=[10,-20,-289,100]

for temperature in temperatures:
 	if temperature >= -273:
 		print(celsius_to_fah(temperature))
 	else:
 		print("not possible")