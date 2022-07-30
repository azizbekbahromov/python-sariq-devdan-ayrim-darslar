son = 0
while son<=9: 
    print(son, end=' ',) 
    son = son+1

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'chiqish' deb yozing): "
qiymat = ''
while True: 
    qiymat = input(savol)
    if qiymat == 'chiqish':
        break 
    else:
        print(float(qiymat)**2)