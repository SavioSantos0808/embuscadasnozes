import random
import time


#Posição dos personagens
posicao = []

#Movimentos
quantpassos = 0
sementespegas = 0

#Mapa do jogo
mapa = []
for a in range(10):
    lista = []
    for b in range(10):
        lista.append(".")
    mapa.append(lista)

def boasvindas():
    saudacao = print("Bem-vindo(a) ao jogo \"Em Busca das NOZES\".\nInfelizmente, todas as NOZES do mundo foram extintas",
                     "e agora só restam 4\nvariedades de nozes escondidas em baixo de geleiras na Antártida, que",
                     "foram\nguardadas por pesquisadores. Fizeram isso, porque premeditaram uma possível\nextinção",
                     "de algumas espécies de plantas no futuro.",
                     "\nEnfim. Encontre-as para replantá-las no mundo.\n", 
                     "\nVamos lá!!! Encontre as rotas mais rápidas\npara terminar o jogo com menos passos.\n")
def instrucoes():
    exemplo = print("Escreva o sentido que você quer fazer assim:",
                    "\nExemplo: D (Mova para a direita).\n")
    comandos = print("D ou d - move para direita.\nE ou e - move para esquerda.\nC ou c - move para cima.\nB ou b - move para baixo.")

def imprimirmapa():
    for x in range(10):
        print(str(mapa[x][:]).strip("[]").replace(",","").replace("'",""))

def posicaopersonagem(posicao):
    posicao = (random.sample(range(0,10),10))
    return posicao

posicao = posicaopersonagem(posicao)

boasvindas()
imprimirmapa()

indice = 2
while indice <= 9:
    mapa[posicao[indice]][posicao[indice+1]] = "$"
    indice += 2
    
print("\nSe localizando no mapa... \nLembre-se você é o X e as sementes os $.\n")
time.sleep(4)
inicio = input("Começar? sim ou nao: ")
print("\n\n")

if inicio == "SIM" or inicio == "sim" or inicio == "Sim":
    while True:
        mapa[posicao[0]][posicao[1]] = "X"    
        instrucoes()
        print("\nPASSOS: {0}\n".format(quantpassos))
        imprimirmapa()
        comandos = input("\nDigite o comando: ")
        if comandos == "D" or comandos == "d":
            casa1 = posicao[1]
            mapa[posicao[0]][casa1] = "."
            if posicao[1] + 1 > 9:
                print("Não pode ultrapassar aqui.")
                time.sleep(2)
            else:
                posicao[1] += 1
                quantpassos += 1
        if comandos == "E" or comandos == "e":
            casa1 = posicao[1]
            mapa[posicao[0]][casa1] = "."
            if posicao[1] - 1 < 0:
                print("Não pode ultrapassar aqui.")
                time.sleep(2)
            else:
                posicao[1] -= 1
                quantpassos += 1
        if comandos == "C" or comandos == "c":
            casa1 = posicao[0]
            mapa[casa1][posicao[1]] = "."
            if posicao[0] - 1 < 0:
                print("Não pode ultrapassar aqui.")
                time.sleep(2)
            else:
                posicao[0] -= 1
                quantpassos += 1
        if comandos == "B" or comandos == "b":
            casa1 = posicao[0]
            mapa[casa1][posicao[1]] = "."
            if posicao[0] + 1 > 9:
                print("Não pode ultrapassar aqui.")
                time.sleep(2)
            else:
                posicao[0] += 1
                quantpassos += 1

        for a in range(10):
            for b in range(10):
                if mapa[a][b] == "$":
                    sementespegas += 1
       
        if sementespegas == 0:
            print("\n\nFim de Jogo. Você conseguiu coletar todas as sementes.")
            print("\nQuantidade de passos: {0}".format(quantpassos))
            time.sleep(5)
            break
        else:
            sementespegas = 0
                
        
else:
    print("Ok. Até mais!")
