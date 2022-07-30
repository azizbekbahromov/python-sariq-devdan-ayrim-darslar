narh = 15000 
choy = True 
salat = False

if choy and salat: 
    narh = narh + 10000 
elif choy or salat: 
    narh = narh + 5000  
print(narh)    
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')