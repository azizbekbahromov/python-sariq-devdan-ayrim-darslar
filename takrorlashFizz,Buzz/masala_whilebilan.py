son =0
while son<=100:  
    son = son+1
    if son%3==0 and son%15!=0:
        print("Fizz",end=' ',)
    elif son%5==0 and son%15!=0:
        print("Buzz",end=' ',)    
    elif son%15==0:
        print("FuzzBuzz",end=' ',)
    else:
        print(son, end=' ',) 


        
