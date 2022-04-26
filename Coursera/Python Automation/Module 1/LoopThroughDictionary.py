wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth,colors in wardrobe.items():
	for color in colors:
		print("{color} {cloth}".format(cloth = cloth,color = color))