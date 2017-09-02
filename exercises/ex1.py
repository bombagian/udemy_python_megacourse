def celsius_to_fah(celsius):
	fah=int(celsius)*9/5+32
	return fah

c = input("Insert temp. in celsius: ")
print(celsius_to_fah(c))