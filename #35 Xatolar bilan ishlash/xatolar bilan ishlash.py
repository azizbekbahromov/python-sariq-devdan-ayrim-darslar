import json
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)  
    print(f"Siz {2021-yosh} yilda tug'ilgansiz")  
except:
    print("Butun son kiritmadingiz")

print("Dastur Tugadi!")

n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError: 
    print("Butun son kiritmadingiz")
except ZeroDivisionError: 
    print("0 ga bo'lib bo'lmaydi")
else:
  print(f"x={x}")

filename = "data.txt" 
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"Kechirasiz, {filename} fayli mavjud emas. Bosh fayl tanlang.")