#Loading...Férias
import random
import os
import time
  
lista = []
def tempo():
    time.sleep(5)

for i in range(51):
    lista.append(i)
      
def exibirnumeros(lista):
    #exibição dos números 
    ini = 0
    fim = 11
    d = 5
    if len(lista) <= 11:
        d = 1
    elif len(lista) <= 22:
        d = 2
    elif len(lista) <= 33:
        d = 3
    elif len(lista) <= 44:
        d = 4
          
    for x in range(d):
        print(lista[ini:fim], end="")
        print("")
        ini += 11
        fim += 11
        #fim da exibição dos números
 
def executar(lista,menor_numero_inserido,maior_numero_inserido,numeros_digitados):
    while True:
        if len(lista) == 3: 
            exibirnumeros(lista)
            print("\nImprenssado!")
            break
        elif len(lista) == 1:
            exibirnumeros(lista)
            print("\nImprenssado!")
            break
            continue
      
        else:
            os.system("cls")
            print("\nEscolha um número entre %s e %s: "%(lista[0],lista[-1]))
            exibirnumeros(lista)
            tent=int(input("\nTente: "))

 
            if tent == numero:
                print("\nAcertou(%d)!\n Pode Beber!"%numero)
                break
 
            elif tent in numeros_digitados:
                print("Você já tentou esse número! Tente novamente!")
                tempo()
                print("Em 5 segundos você poderá tentar novamente!")
                continue
 
            elif tent < menor_numero_inserido or tent > maior_numero_inserido:
                print("Tentativa inválida! Tente novamente")
                tempo()
                print("Em 5 segundos você poderá tentar novamente!")
                continue
      
            elif tent > numero:
                maior_numero_inserido = tent
 
            elif tent < numero:
                menor_numero_inserido = tent+1
 
            lista = [i for i in range(menor_numero_inserido,maior_numero_inserido)]
            numeros_digitados.append(tent)
  
while True:
    menor_numero_inserido = 0
    maior_numero_inserido = 52
    numeros_digitados = []
    opc= input("\n'S' Para sortear o número \n'E' Para escolher \n'X'Sair\nOpção: ")
    if (opc == "E") or (opc == "e"):
        numero= int(input("Digite um número: "))
        os.system("cls")
        executar(lista,menor_numero_inserido,maior_numero_inserido,numeros_digitados)       
      
    elif (opc == "S") or (opc == "s"):
        numero= random.randint(0,50)
        os.system("cls")
        executar(lista,menor_numero_inserido,maior_numero_inserido,numeros_digitados)
 
    elif opc == "X" or opc == "x":
        print("Saindo...")
        break
         
    else:
        print("Opção inválida!")
