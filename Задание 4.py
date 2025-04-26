line = input("Введите строку: ")
if line.startswith("abc"):
    line = line.replace("abc", "www")
else:
    line = line + "zzz"

print(line)
