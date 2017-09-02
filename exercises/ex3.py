def celsius_to_fah(celsius):
	fah=int(celsius)*9/5+32
	return fah

c = float(input("Insert temp. in celsius: "))
min = float(-273)

if c >= -273:
	print(celsius_to_fah(c))
else:
	print("not possible")