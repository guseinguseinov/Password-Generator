import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("[+] Welcome to Password Generator.")
letters_num = int(input("[+] How many letters would you like in your password?"))
numbers_num = int(input("[+] How many numbers would you like in your password?"))
symbols_num = int(input("[+] How many symbols would you like in your password?"))

lns_list = []
for i in range(0, letters_num):
    lns_list.append(random.choice(letters))

for i in range(0, numbers_num):
    lns_list.append(random.choice(numbers))

for i in range(0, symbols_num):
    lns_list.append(random.choice(symbols))

random.shuffle(lns_list)
passwd = "".join(lns_list)
print(f"[+] Your password :{passwd}")