from ast import Break


def toliq_ism_yasa(ism, familiya):
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism 

talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('hakim','olimov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    
    if otasining_ismi: 
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
talaba1 = toliq_ism_yasa('Azizbek','Bahromov') 
talaba2 = toliq_ism_yasa('Said',"Og'abekov",'Otabekovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
def avto_info(kompaniya, model,motor, rangi, karobka, ot_kuchi, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'motor':motor,
            'rang':rangi,
            'karobka':karobka,
            'ot_kuchi':ot_kuchi,
            'yili':yili,
            'narh':narhi}
    return avto
avto1=avto_info("Avtovaz","Lada Largus","Germanskiy Reno","oq","mexanika","102ta","2014","10000$")
avto2=avto_info("General Motors Uz","Malibu","2.4 atmosferniy gm_uz","oq","Avtomat","269ta","2013",)
avtolar=[avto1,avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}, {avto['karobka']} karobkali {avto['yili']}yilgi Narhi: {narh}")

def oraliq(min,max,qadam):
    sonlar = [] 
    while min<max:
        sonlar.append(min)
        min += 1
        
        
    return sonlar

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    motor=input("Motori:")
    rangi=input("Rangi: ")
    karobka=input("Korobka: ")
    ot_kuchi=input("Ot-kuchi")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model,motor, rangi, karobka, ot_kuchi, yili, narhi=None))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    
    if javob=='no':
         break
  