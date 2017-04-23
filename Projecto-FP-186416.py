#Francisco Sousa 86416
import math

#------------------------------VERSAO SIMPLIFICADA------------------------------
def gera_chave1(letras):
    '''Recebe um tuplo de 25 caracteres e devolve 5 tuplos de 5 elementos
    usando ciclos for para percorrer cada linha, e adicionar cada elemento a
    ela, formando uma chave'''
    chave = ()
    for ln in range(5):
        linha = ()
        for cl in range(5):
            linha = linha + (letras[cl + 5*ln],)
        chave = chave + (linha,)
    return(chave)

def obtem_codigo1(car, chave):
    '''Recebe uma chave e um caracter. Procura-o na chave e devolve a posicao'''
    for ln in range(len(chave)):
        for cl in range(len(chave[ln])):
            if chave[ln][cl] == car:
                return str(ln) + str(cl)
            
def codifica1(cad, chave):
    '''Recebe uma chave e uma sequencia de caracteres. Usa a obtem_codigo1 para
    devolver a codificacao dos caracteres'''
    cod = ""
    for car in range(len(cad)):
        cod = cod + obtem_codigo1(cad[car], chave)
    return cod

def obtem_car1(cod, chave):
    '''Recebe uma chave e um codigo de caracter, que corresponde a posicao dele
    na chave. Devolve o caracter'''
    return chave[eval(cod[0])][eval(cod[1])]

def descodifica1(cad_codificada, chave):
    '''Recebe uma chave e uma sequencia de caracteres numericos. Usa a funcao 
    obtem_car1 para devolver a cadeia de carateres correspondente a sequencia'''
    cad = ""
    for cod in range(0, len(cad_codificada), 2):
        cad = cad + obtem_car1(cad_codificada[cod] + cad_codificada[cod+1], chave)
    return cad


#---------------------------------VERSAO FINAL----------------------------------
def gera_chave2(letras):
    '''Recebe um tuplo de caracteres, e devolve uma chave. Usa a funcao auxiliar
    no_tuplos para calcular o numero de tuplos dentro desta chave e a funcao
    no_elementos para calcular o numero de elementos dentro de cada um destes'''
    chave = ()
    n_tpl = no_tuplos(letras)
    n_el = no_elementos(letras, n_tpl)
    for t in range(n_tpl):
        chave = chave + (letras[ n_el*t : n_el*(t + 1) ],)
    return chave

def no_tuplos(letras):
    '''Recebe um tuplo letras. Devolve a raiz quadrada do seguinte quadrado
    perfeito igual ou superior ao comprimento do tuplo'''
    sqrtl = int(math.sqrt(len(letras)))
    if sqrtl**2 == len(letras):
        return sqrtl
    else:
        return sqrtl + 1

def no_elementos(letras, n_tuplos):
    '''Recebe o tuplo letras e o numero de tuplos calculado pela funcao
    no_tuplos. Se o comprimento de letras for igual ou inferior ao n_tuplos
    elevado ao quadrado menos o numero de tuplos, quer dizer que, para uma 
    matriz com n_tuplos linhas e n_tuplos colunas, so haveria caracteres
    suficientes para preencher todas as linhas menos a ultima. Assim neste caso,
    devolve n_tuplos - 1'''
    if len(letras) > n_tuplos*(n_tuplos - 1):
        return n_tuplos
    else:
        return n_tuplos - 1
    
def obtem_codigo2(car, chave):
    '''Recebe uma chave e um caracter. Usa o obtem_codigo1 para o procurar na
    chave e devolve a posicao/codificacao dele. Se nao estiver contido na chave,
    devolve "X"'''
    if not obtem_codigo1(car, chave):
        return "XX"
    else:
        return obtem_codigo1(car, chave)

def codifica2(cad, chave):
    '''Recebe uma chave e uma sequencia de caracteres. Usa a obtem_codigo2 para
    devolver a codificacao dos caracteres'''
    cod = ""
    for car in range(len(cad)):
        cod = cod + obtem_codigo2(cad[car], chave)
    return cod

def obtem_car2(cod, chave):
    '''Recebe uma chave e um codigo de caracter, que corresponde a posicao dele
    na chave. Usa a obtem_car1 para devolver o caracter. Se o codigo do caracter
    for "X", devolve um "?"'''
    if cod == "XX":
        return "?"
    else:
        return obtem_car1(cod, chave)

def descodifica2(cad_codificada, chave):
    '''Recebe uma chave e uma sequencia de caracteres numericos. Usa a funcao 
    obtem_car2 para devolver a cadeia de carateres correspondente a sequencia'''
    cad = ""
    for cod in range(0, len(cad_codificada), 2):
        cad = cad + obtem_car2(cad_codificada[cod] + cad_codificada[cod + 1], chave)
    return cad