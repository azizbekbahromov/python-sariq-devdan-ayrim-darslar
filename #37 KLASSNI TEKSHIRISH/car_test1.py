
import unittest
from cars import Car

make = "GM"
model = "Malibu"
year = 2020
km = 10
price = 40000
avto = Car(make, model, year, km, price)


class CarTest(unittest.TestCase):
  

    def test_create(self):
   
        avto1 = Car("toyota", "camry", 2020)
   
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
    
        self.assertIsNone(avto1.price)
      
        self.assertEquals(0, avto1.get_km())
        
        avto2 = Car("toyota", "camry", 2020, price=75000)
        self.assertEquals(75000, avto2.price)


unittest.main()