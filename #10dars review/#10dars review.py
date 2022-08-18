avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar: 
    if avto == 'bmw': 
        print(avto.upper())
    else: 
        print(avto.title())

ism = input('Ismingiz nima?\n>>>') 
if ism.lower() != 'ali': 
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.")
else:
    print("Salom, Ali")
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")