import random
#############################################   IMPORTS   ##############################################################




############################################# CLASSE UNICORNIO  ########################################################
class Unicornio:
    def __init__(self,nome, cor_rabo, tamanho, cor_corpo, portador, alimentação):
        self.nome = nome
        self.cor_rabo = cor_rabo
        self.tamanho = tamanho
        self.cor = cor_corpo
        self.portador = portador
        self.alimentacao = alimentação


    def menudejogo (self):
      input("Escolha uma opção: ")

    def pergunta1 (self):
        userdois = input(f"Voce acabou de adotar um unicornio chamado {nome}.agora vamos alimenta-lo.aperte dar comida para alimenta-lo  ").lower()
        if userdois == "Dar comida":
              print(f"{portador} e {nome} foram voar perto da montanha bosch")
        else:
            print(f"nenhuma opção foi selecio")
            return

    print("=" * 20)

    def pergunta2 (self):
        usertres = input(f"No caminho pra casa {nome} quer voar em alta velocidade,você aceita? ").lower()
        if usertres == "Não":
           print("Vocês dois chegaram salvos em casa")
        else:
            print("Vocês dois bateram na caixa d'agua e morreram...")
            exit()



################################################# PRINTS ###############################################################

print("FABRICA DE UNICORNIO D JÃ1")
print("~-" *13)
print("=" * 20)
nome = input("Qual vai ser o nome dele(a)? ")
print("=" * 20)
cor_corpo = input("Qual irá ser a cor do corpo? ")
print("=" * 20)
cor_rabo = input("Qual vai ser a cor do rabo? ")
print("=" * 20)
alimentacao = input("O que ele(a) vai comer? ")
print("=" * 20)
tamanho = input("Qual vai ser o tamanho dele(a)? ")
print("=" * 20)
portador = input("Quem irá montar nele(a)? ")
print("=" * 20)
print(f"Parabens voce criou seu primeiro unicornio! agora vamos ver qual irá ser sua personalidade")
personalidades = ['Alegre','Revoltado','Bad boy','Festeiro','Crossfiteiro','inteligente','Carente','Engraçado','Preguiçoso','ranzinza']
print("=" * 20)
print("Personalidade: " + personalidades [random.randrange(len(personalidades))])
print("=" * 20)


print("BEM VINDO AO REINO MAGICO DOS UNICORNIOS")
print("1-Começar historia")
print("2-Fechar jogo")

# PARA PRINTAR

unicornio = Unicornio(nome, cor_rabo, tamanho, cor_corpo, portador, alimentacao)

unicornio.menudejogo()


unicornio.pergunta1()

unicornio.pergunta2()
