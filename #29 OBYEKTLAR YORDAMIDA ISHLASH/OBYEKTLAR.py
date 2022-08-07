class Talaba:

    def __init__(self, ism, familiya, tyil):
    
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_name(self):
        return self.ism

    def get_info(self):
       
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def set_bosqich(self, bosqich):
        
        self.bosqich = bosqich

    def update_bosqich(self):
      
        self.bosqich += 1

    def get_name(self):
        return self.ism

    def get_lastname(self):
      
        return self.familiya

    def get_fullname(self):
        
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        
        return yil - self.tyil

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")


talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_info())
talaba1.update_bosqich() 
print(talaba1.get_info())
talaba1.update_bosqich() 
print(talaba1.get_info())

talaba1.set_bosqich(3)
print(talaba1.bosqich)