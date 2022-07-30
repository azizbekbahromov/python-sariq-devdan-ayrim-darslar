talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")
talaba_0['kurs'] = 4 
talaba_0['fakultet'] = 'informatika' 
print(talaba_0)
 
talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

telefonlar = {
    'ali':'iphone x',
    'vali':'samsung galaxy s10',
    'olim':'xiami 12 pro plus',
    'orif':'remdi note11'
    }
phone = telefonlar['ali']
print(f"Alining telefoni {phone}")
phone = telefonlar['hasan']
print(f"Hasanning telefoni {phone}")

