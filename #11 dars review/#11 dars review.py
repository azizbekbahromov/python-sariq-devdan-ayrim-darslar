yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
    print("Cho'milgani ketdik!")
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
    print("Uyda dam olamiz!")

narh = 15000 
choy = True
salat = False
non = True
kompot = True
assorti = False

if choy:  
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot:
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: 
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')