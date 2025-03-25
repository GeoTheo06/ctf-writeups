flag = "picoCTF{"
import string
flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
for i in len(flag):
	for char1 in string.printable:
		for char2 in string.printable:
			test = chr((ord(char1) << 8) + ord(char2))
			if (test == )
		print(test)

res1 = chr((ord(test[0]) - ord('i')) >> 8)
res2 = ord(test[0]) - (ord('P') << 8)
print(res2)