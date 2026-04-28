def mAritmetica(n1,n2,n3):
    media=(n1+n2+n3)/3
    return media

def mPonderada(n1,n2,n3):
    media=((2*n1)+(3*n2)+(4*n3))/9
    return media

def mHarmonica(n1,n2,n3):
    media=(3/((1/n1)+(1/n2)+(1/n3)))
    return media

n1=float(input("Entre com o primeiro número: "))
n2=float(input("Entre com o segundo número: "))
n3=float(input("Entre com o terceiro número: "))

tipo=int(input("Digite \n 1 - para media aritmetica.\n 2 - para ponderada.\n 3 - media harmonica. \n :"))

if tipo!=1 and tipo!=2 and tipo!=3:
    print("Entrada invalida")
 
else:
    if tipo==1:
        m=mAritmetica(n1,n2,n3)
 
    elif tipo==2:
        m=mPonderada(n1,n2,n3)
 
    else:
        m=mHarmonica(n1,n2,n3)
     
         
    print("A media é {: .2f}".format(m))