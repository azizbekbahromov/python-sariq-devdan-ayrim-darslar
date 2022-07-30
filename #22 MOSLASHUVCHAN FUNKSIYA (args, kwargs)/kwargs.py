def avto_info(yili,modeli,matori,**malummotlar):
    malummotlar['Yili']=yili
    malummotlar['Modeli']=modeli
    malummotlar['Matori']=matori
    return malummotlar
avto1=avto_info(2013,'Malibu','2.4atmosferniy',rangi='oq',ot_kuchi='269hp')
avto2=avto_info(2007,'Lacceti','1.8 atmosferniy',rangi='oq',ot_kuchi='105hp',narxi='9000$')