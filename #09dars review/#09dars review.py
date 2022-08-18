mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print('Salom',mehmon)
    print("hayr",mehmon)
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")
sonlar = list(range(1,11))
sonlar_kvadrati=[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)

dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): 
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)
    
