import numpy as np
def sort_doors():
    doors=['goat','goat','car']
    return(np.random.permutation(doors))
def choose_door():
 return np.random.choice([0,1,2])
def reveal_door(lista, choice):
    i=0
    j=1
    while(j!=0):
        if(i!=choice and lista[i]=='goat'):
            lista[i]='MONT'
            j=0
        i+= 1
    return(lista)
def finish_game(lista,choice,change):
    if(change==True):
        j=1
        i=0
        while(j!=0):
            if(i!=choice and lista[i]!='MONT'):
                j=0
                return(lista[i])
            i+=1
    else:
        return (lista[choice])
ganadasSinCambio=0
SinCambio=list()
ganadasConCambio=0
ConCambio=list()
for k in range(100):
    Choice=choose_door()
    Boo=finish_game(reveal_door(sort_doors(),Choice),Choice,False)
    SinCambio.append(Boo)
    if(Boo=='car'):
        ganadasSinCambio+= 1
for o in range(100):
    Choice=choose_door()
    listt=reveal_door(sort_doors(),Choice)
    Boo=finish_game(listt,Choice,True)
    ConCambio.append(Boo)
    if(Boo=='car'):
        ganadasConCambio+=1
print('la probabilidad de ganar sin cambiar de puerta es: ',ganadasSinCambio/100,'la probabilidad de ganar cambiando de puerta es: ',ganadasConCambio/100)

