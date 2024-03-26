file = open("sample_text.txt")
contents = file.read()
print(contents)
file.close()

with open("sample_text.txt", mode="w") as file:
    file.write("\nI am 25 years old.")
    file.write("\nI like python.")

with open("sample_text.txt") as file:
    contents = file.read()
    print(contents)
