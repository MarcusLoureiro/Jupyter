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

def CalculaResultado(Ccache, Nb, Cmp, conjuntos):
    '''Quantidade de linhas'''
    Linhas = Ccache/Nb
    
    '''Quantidade de Conjuntos'''
    Conjuntos = Linhas/conjuntos
    
    '''Quantidade de blocos'''
    Blocos = Cmp/Nb
    
    '''Largura do campo tag'''
    tag = math.log2((Blocos/Conjuntos))
    
    '''Largura do campo conjunto'''
    conjunto = math.log2((Conjuntos))
    
    '''Total de bits da celula'''
    celula = math.log2((Nb))
    
    
    print("\nFormato de endereço da cache com mapeamento associativo por conjunto"+
      "de",conjuntos,":\n| Tag      |",tag," bits\n| Conjunto |",conjunto," bits"+
      "\n| Byte     |",celula," bits\nTotal de bits do endereço: ",
      (tag+conjunto+celula)," bits")

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

conjuntos = int(input("Informe quantas linhas em cada conjunto: ")) 
    
print(CalculaResultado(Ccache, Nb, Cmp, conjuntos))

