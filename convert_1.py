def read_file(filename):
	lines = []
	with open(filename, "r") as f:
		for line in f:
			lines.append(line.strip())
	return lines	


def convert(lines):
	Aaron_word = 0
	Blet_word = 0
	Aaron_picture = 0
	Blet_picture = 0
	for line in lines:
		s = line.split(" ")
		if s[1] == "Aaron":
			if s[2] == "貼圖":
				Aaron_picture = Aaron_picture + 1
			else:
				for m in s[2:]:
					Aaron_word = Aaron_word + len(m)	

		elif s[1] =="blet":
			if s[3] == "貼圖":
				Blet_picture = Blet_picture + 1
			else:
				for m in s[3:]:
					Blet_word = Blet_word + len(m)	
	print("Aaron一共講了", Aaron_word, "個字")
	print("Blet一共講了", Blet_word, "個字")
	print("Aaron一共貼了", Aaron_picture, "張貼圖")
	print("Blet一共貼了", Blet_picture, "張貼圖")

def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n") 


def main():
	lines = read_file("[Line]YT.txt")
	print(lines)
	convert(lines)
	#write_file("output.txt", lines)

main()	