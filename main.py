words = []
status = "on"

print("List words in alphabetical order. Leave input empty (write nothing and press ENTER) to end proecss.")

print("""\nWhat should be prioritised?
\t[A] Lowercase letters
\t[B] Uppercase letters
""")

choice = input("Choice (A or B): ")
print("\n")

while status == "on":
	word = input("Word: ")
	if word == "":
		status = "off"
	else:
		words.append(word)

if choice == "A":
	words.sort(key=str.lower)
else: 
	words.sort(key=str.upper)

print("==========================")

for i in words:
	print(i)

