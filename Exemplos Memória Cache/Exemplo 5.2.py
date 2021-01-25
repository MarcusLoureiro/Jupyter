import math
aviso = '''ERRO - DADO INCORRETO, TENTE NOVAMENTE:'''

def ValidaEntrada(b):
    for i in range(len(b)):
        if(b[i] == "B"):
            return True
            break
        elif(b[i]+b[i+1]=="KB"):
            return True
            break
        elif(b[i]+b[i+1]=="MB"):
            return True
            break
        elif(b[i]+b[i+1]=="GB"):
            return True
            break
        elif(b[-1] != "B"):
            return False

def CalculaBase(b):
    valor = ""
    resultado = 1
    for i in range(len(b)):
        if(b[i] == "B"):
            break
        elif(b[i] == "K"):
            resultado = 2**10
            break
        elif(b[i] == "M"):
            resultado = 2**20
            break
        elif(b[i] == "G"):
            resultado = 2**30
            break
        else: valor = valor + b[i]
    
    return (int(valor))*resultado

def InverteBase(b):
    if((b%(2**30)) == 0):
        return str(b/(2**30))+"GB"
    elif((b%(2**20)) == 0):
        return str(b/(2**20))+"MB"
    elif((b%(2**10)) == 0):
        return str(b/(2**10))+"KB"
    else:
        return str(b)+"B"

def CalculaResultado(Ccache, Nb, Cmp):
    '''Total de bits de dados'''
    Tdados = Ccache*8
    '''Quantidade de linhas'''
    Linhas = Ccache/Nb
    '''Quantidade de blocos'''
    Blocos = Cmp/Nb
    '''Largura do campo tag'''
    tag = math.log2((Blocos/Linhas))
    '''Total de bits dos tags'''
    Ttag = Linhas*tag
    '''Total de bits da cache'''
    Tcache = Tdados + Ttag
    return (InverteBase(Tcache))
    

Ccache = input('''Digite a capacidade da memóra cache:
Ex: 32KB
Digite aqui:''')

while True:
    if(ValidaEntrada(Ccache)):
        Ccache = CalculaBase(Ccache)
        break
    else:
        print(aviso)
        Ccache = input('''Digite a capacidade da memóra cache:
Ex: 32KB
Digite aqui:''')

Nb = input('''Digite o número de células por linha da memória cache:
Ex: 8B
Digite aqui:''')        
while True:
    if(ValidaEntrada(Nb)):
        Nb = CalculaBase(Nb)
        break
    else:
        print(aviso)
        Nb = input('''Digite o número de células por linha da memória cache:
Ex: 8B
Digite aqui:''')


Cmp = input('''Informe a capacidade de células(bytes) da memória principal:
Ex: 16MB
Digite aqui:''')        
while True:
    if(ValidaEntrada(Cmp)):
        Cmp = CalculaBase(Cmp)
        break
    else:
        print(aviso)
        Cmp = input('''Informe a capacidade de células(bytes) da memória principal:
Ex: 16MB
Digite aqui:''')
    
print(CalculaResultado(Ccache, Nb, Cmp))

