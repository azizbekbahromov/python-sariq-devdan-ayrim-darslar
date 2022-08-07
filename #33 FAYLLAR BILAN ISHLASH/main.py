import pickle

with open('amaliyot/pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n','') 
pi = pi.replace(' ','')

# Tug'ilgan kunim pi da bormi?
bdate = '31122000'
print(bdate in pi)

pi = float(pi) 

with open('amaliyot/pi_float.dat','wb') as file:
    pickle.dump(pi,file)

while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('books.txt','a') as file:
        file.write(book+'\n')
