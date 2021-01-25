import math
aviso = '''ERRO - DADO INCORRETO, TENTE NOVAMENTE:'''

def TestaEndereco(endereco):
  retorno = None
  for i in range(4):
    if(endereco[i] != "0" and endereco[i] != "1"):
      retorno = False
      return False
    else:
      retorno = True
  if(retorno):
    return True
  else:
    return False
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


def CalculaResultado(Lblocos, NCache, Endereco):
  
  '''Bits da celula'''
  celula = math.log2(Lblocos)
  
  '''Quantidade de blocos'''
  Blocos = (2**(len(Endereco)*4))/Lblocos

  '''Bits do campo bloco'''
  Bloco = math.log2(Blocos)

  '''Endereço em binário'''
  Abin = HexParaBinario(Endereco)
  Abloco = ""
  Acelula = ""
  for i in range(len(Abin)):
    if(i>=0 and i<Bloco):
      Abloco = Abloco + Abin[i]
    elif(i>=Bloco):
      Acelula = Acelula + Abin[i]
      
  print("\nFormato de endereço da cache:\n| Bloco |",Abloco,"\n| Byte  |",Acelula,
      "\nEndereço do bloco para acesso: ", Abloco)

Lblocos = input('''Digite a largura dos blocos da memóra principal:
Ex: 16B
Digite aqui:''')

while True:
    if(ValidaEntrada(Lblocos)):
      Lblocos = CalculaBase(Lblocos)
      break
    else:
        print(aviso)
        Lblocos = input('''Digite a largura dos blocos da memóra principal:
Ex: 16B
Digite aqui:''')

NCache = input('''Digite o número de células da memória cache:
Ex: 64KB
Digite aqui:''')        
while True:
    if(ValidaEntrada(NCache)):
      NCache = CalculaBase(NCache)
      break
    else:
      print(aviso)
      NCache = input('''Digite o número de células da memória cache:
Ex: 64KB
Digite aqui:''')  


Endereco = input('''Informe o endereço a ser acessado em Hexadecimal:
Ex: 2A56F
Digite aqui:''')        
    
print(CalculaResultado(Lblocos, NCache, Endereco))

