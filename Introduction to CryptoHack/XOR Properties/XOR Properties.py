key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_key1_key3_key2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1_ord = []
key2_key3_ord = []
FLAG_key1_key3_key2_ord = []
FLAG_key1_ord = []
FLAG_ord = []
for i in bytes.fromhex(key1):
	key1_ord.append(i)

for i in bytes.fromhex(key2_key3):
	key2_key3_ord.append(i)

for i in bytes.fromhex(FLAG_key1_key3_key2):
	FLAG_key1_key3_key2_ord.append(i)

for (ord_flag132, ord23) in zip(FLAG_key1_key3_key2_ord, key2_key3_ord):
	FLAG_key1_ord.append(ord_flag132 ^ ord23)


for (ord_flag1, ord1) in zip(FLAG_key1_ord, key1_ord):
	FLAG_ord.append(ord_flag1 ^ ord1)
flag = ""

for i in FLAG_ord:
	flag += chr(i)
print(flag)
