string = "label"
num = 13
flag=""
for i in string:
	a = [ord(i)]
	for j in a:
		c = 13 ^ j
		d = chr(c)
		flag += (d)
print("crypto{"+flag+"}")
