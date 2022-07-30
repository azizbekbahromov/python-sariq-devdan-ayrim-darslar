def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism.title()} ga baho qo'ying:" )
        baholar[ism]=int(baho)
    return baholar
talabalar=["aziz","temur","ali","said"]
baholar=bahola(talabalar[:])
print(baholar)
print(talabalar)
