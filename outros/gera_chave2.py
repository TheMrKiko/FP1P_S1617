import math
def teste(letras):
    tuplo=()
    n_tpl=no_tuplos(letras)
    n_el=no_elementos(letras, n_tpl)
    for t in range(n_tpl):
        tuplo+=(letras[t*n_el:(t+1)*n_el],)
    return tuplo

def no_tuplos(letras):
    sqrtl=int(math.sqrt(len(letras)))
    if sqrtl**2 == len(letras):
        return sqrtl
    else:
        return sqrtl+1

def no_elementos(letras, no_tuplos):
    if len(letras)>no_tuplos*(no_tuplos-1):
        return no_tuplos
    else:
        return no_tuplos-1
    
teste(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q',"F"))