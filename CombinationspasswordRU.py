import random

spisok = [
    "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F",
    "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L",
    "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R",
    "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X",
    "y", "Y", "z", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
user = "yes"
def main():
	while True:
		print("Напишите yes для продолжения")
		user = input()
		if user == "yes":
			randomizer = random.choices(spisok, k=10)
			print("".join(randomizer))
		else:
			print("ошибка, нет другого выбора")


main()


