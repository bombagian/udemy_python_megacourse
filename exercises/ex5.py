def celsius_to_fah(celsius):
	if temperature >= -273:
		fah=int(celsius)*9/5+32
		return fah
	#else: return "n"




temperatures=[10,-20,-289,100]

file=open("c_to_f.txt","w")
for temperature in temperatures:
	print(celsius_to_fah(temperature))
	if(celsius_to_fah(temperature) != None):
		file.write(str(celsius_to_fah(temperature))+"\n")
	
file.close()
