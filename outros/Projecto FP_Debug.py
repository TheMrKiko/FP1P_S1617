#Francisco Sousa 86416
import math

letras=()
for car in range(65,92):
    if car==ord('K'):
        letras+=(" ",)
    elif car==91:
        letras+=(".",)
    elif not (car==ord('W') or car==ord('Y')):
        letras+=(chr(car),)
    
def gera_chave1(letras):
    chave=()
    for l in range(5):
        linha=()
        for c in range(5):
            linha+=(letras[c+5*l],)
        chave+=(linha,)
    return(chave)

chave=gera_chave1(letras)
print(chave)

def obtem_codigo1(car,chave):
    for l in range(5):
        for c in range(5):
            if chave[l][c]==car:
                return str(l)+str(c)
print(obtem_codigo1("Q",chave))
            
def codifica1(cad,chave):
    cod=""
    for car in range(len(cad)):
        cod+=obtem_codigo1(cad[car],chave)
    return cod
print(codifica1("FU",chave))

def obtem_car1(cod,chave):
    return chave[eval(cod[0])][eval(cod[1])]
print(obtem_car1("31",chave))

def descodifica1(cad_codificada,chave):
    cad=""
    for cod in range(0,len(cad_codificada),2):
        cad+=obtem_car1(cad_codificada[cod]+cad_codificada[cod+1],chave)
    return cad
print(descodifica1("1040",chave))

import math

def gera_chave2(letras):
    chave=()
    n_tpl=no_tuplos(letras)
    n_el=no_elementos(letras, n_tpl)
    for t in range(n_tpl):
        chave+=(letras[n_el*t:n_el*(t+1)],)
    return chave

def no_tuplos(letras):
    sqrtl=int(math.sqrt(len(letras)))
    if sqrtl**2 == len(letras):
        return sqrtl
    else:
        return sqrtl+1

def no_elementos(letras, n_tuplos):
    if len(letras)>n_tuplos*(n_tuplos-1):
        return n_tuplos
    else:
        return n_tuplos-1
    
chave=gera_chave2(("A","B","C","D","E","F","G","H","I","J","L","M","N","O","P","Q","R","S","T","U","V","X","Z"))
print(chave)

def obtem_codigo2(car,chave):
    for l in range(len(chave)):
        for c in range(len(chave[l])):
            if chave[l][c]==car:
                return str(l)+str(c)
    return "XX"
print(obtem_codigo2("Q", chave))
print(obtem_codigo2(":", chave))

def codifica2(cad,chave):
    cod=""
    for car in range(len(cad)):
        cod+=obtem_codigo2(cad[car],chave)
    return cod
print(codifica2("FU",chave))
print(codifica2("F P",chave))

def obtem_car2(cod,chave):
    if cod == "XX":
        return "?"
    else:
        return obtem_car1(cod,chave)
print(obtem_car2("30",chave))
print(obtem_car2("XX",chave))

def descodifica2(cad_codificada,chave):
    cad=""
    for cod in range(0,len(cad_codificada),2):
        cad+=obtem_car2(cad_codificada[cod]+cad_codificada[cod+1],chave)
    return cad
print(descodifica2("1034",chave))
print(descodifica2("10XX24",chave))