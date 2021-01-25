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

def HexParaBinario(n):
  b = ""
  for i in range(len(n)):
    if(n[i] == "0"):
      b = b + "0000"
    elif(n[i] == "1"):
      b = b + "0001"
    elif(n[i] == "2"):
      b = b + "0010"
    elif(n[i] == "3"):
      b = b + "0011"
    elif(n[i] == "4"):
      b = b + "0100"
    elif(n[i] == "5"):
      b = b + "0101"
    elif(n[i] == "6"):
      b = b + "0110"
    elif(n[i] == "7"):
      b = b + "0111"
    elif(n[i] == "8"):
      b = b + "1000"
    elif(n[i] == "9"):
      b = b + "1001"
    elif(n[i] == "A"):
      b = b + "1010"
    elif(n[i] == "B"):
      b = b + "1011"
    elif(n[i] == "C"):
      b = b + "1100"
    elif(n[i] == "D"):
      b = b + "1101"
    elif(n[i] == "E"):
      b = b + "1110"
    elif(n[i] == "F"):
      b = b + "1111"
  return(b)
  
def converterEndereco(endereco):
  pot = int(0)
  dec = int(0)
  for i in range(len(endereco) - 1, -1, -1):
    dec = dec + pow(2, pot)*int((endereco[i]))
    pot = pot + 1
  return dec

def CalculaResultado(Ccache, LBlocos, Endereco, conjuntos):
  '''Total de bits da celula'''
  celula = math.log2((LBlocos))

  '''Quantidade de linhas'''
  Linhas = Ccache/LBlocos
    
  '''Quantidade de Conjuntos'''
  Conjuntos = Linhas/conjuntos
    
  '''Largura do campo conjunto'''
  conjunto = math.log2((Conjuntos))

    
  '''Bits do campo Tag'''
  tag = (len(Endereco)*4) - conjunto - celula

  '''Endereço em binário'''
  Abin = HexParaBinario(Endereco)
  Atag = ""
  Aconjunto = ""
  Acelula = ""
  for i in range(len(Abin)):
    if(i>=0 and i<tag):
      Atag = Atag + Abin[i]
    elif(i>=tag and i<(tag+conjunto)):
      Aconjunto = Aconjunto + Abin[i]
    elif(i>=(tag+conjunto)):
      Acelula = Acelula + Abin[i]
  print("\nFormato de endereço da cache com mapeamento associativo por conjunto"+
      "de",conjuntos,":\n| Tag      |",Atag,"\n| Conjunto |",Aconjunto,"\n"+
      "| Byte     |",Acelula)

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

LBlocos = input('''Digite a largura dos blocos da memória principal:
Ex: 16B
Digite aqui:''')        
while True:
    if(ValidaEntrada(LBlocos)):
        LBlocos = CalculaBase(LBlocos)
        break
    else:
      print(aviso)
      LBlocos = input('''Digite a largura dos blocos da memória principal
Ex: 16B
Digite aqui:''')   


Endereco = input('''Informe o Endereço a ser acessado em hexadecimal:
Ex: 3FC96
Digite aqui:''')        


conjuntos = int(input("Informe quantas linhas em cada conjunto: ")) 
    
print(CalculaResultado(Ccache, LBlocos, Endereco, conjuntos))

