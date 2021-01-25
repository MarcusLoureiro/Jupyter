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

def CalculaResultado(Cmp, Nb, Lb):
  '''Total de Blocos'''
  Tblocos = Cmp/Nb
  '''Bits da Tag'''
  Bloco = math.log2(Tblocos)
  '''Bits da Célula'''
  celula = math.log2(Nb)
  print("\nFormato de endereço da cache:\n| Bloco |",Bloco," bits\n| Byte  |",
      celula," bits\nTotal de bits do endereço: ",(Bloco+celula)," bits\n"
      +"Número de linhas da cache: ",(Nb))

    

Cmp = input('''Digite a capacidade da memóra principal:
Ex: 32KB
Digite aqui:''')

while True:
    if(ValidaEntrada(Cmp)):
        Cmp = CalculaBase(Cmp)
        break
    else:
        print(aviso)
        Cmp = input('''Digite a capacidade da memóra principal:
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


Lb = input('''Informe o total de linhas da memória cache:
Ex: 4K
Digite aqui:''')        
while True:
    if(ValidaEntrada(Lb)):
        Lb = CalculaBase(Lb)
        break
    else:
        print(aviso)
        Lb = input('''Informe o total de linhas da memória cache:
Ex: 4K
Digite aqui:''')    
    
print(CalculaResultado(Cmp, Nb, Lb))

