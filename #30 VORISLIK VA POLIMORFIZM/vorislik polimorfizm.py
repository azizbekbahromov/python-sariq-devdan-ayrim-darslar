class Shaxs:

    def __init__(self, ism, familiya, passport, tyil):
       
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
      
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
       
        return yil - self.tyil


class Talaba(Shaxs):
  

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
       
        return self.idraqam

    def get_bosqich(self):
       
        return self.bosqich

    def get_info(self):
        
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info


class Manzil:
  

    def __init__(self, uy, kocha, tuman, viloyat):
      
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
      
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


talaba1_manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")
talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil)