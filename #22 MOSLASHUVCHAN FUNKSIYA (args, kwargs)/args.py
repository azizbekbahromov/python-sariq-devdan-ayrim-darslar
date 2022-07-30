def summa(*sonlar):
    yigindi=0
    for son in sonlar:
        yigindi+=son
    return yigindi

def summacha(*sonchalar):
    return sum(sonchalar)
print(summacha(2,5,6))
                      
           