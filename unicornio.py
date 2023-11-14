# IMPORTAR A FUNÇÃO RANDINT

from random import randint


# CRIAÇÃO DA CLASSE UNICÓRNIO COM 5 ATRIBUTOS, SENDO 2 PRIVADOS


class Unicornio:
    # DECLARAÇÃO DO PORTE PADRÃO DO UNICÓRNIO

    porte = "pequeno"

    def __init__(self, nome: str, cor: str, chifre: int, peso: float, velocidade: float):
        self.__nome = nome
        self.cor = cor
        self.chifre = chifre
        self.__peso = peso
        self.velocidade = velocidade

    # CRIAÇÃO DO MÉTODO ESTÁTICO PARA SORTEAR A IDADE DO UNICÓRNIO
    @staticmethod
    def gerarIdade():
        rand = randint(1, 100)
        return f"Ele(a) tem {rand} anos"

    # CRIAÇÃO DO ATRIBUTO ESTÁTICO PARA EXIBIR O PORTE PADRÃO DO UNICÓRNIO
    @staticmethod
    def obter_porte():
        return f"Seu unicórnio é de porte {Unicornio.porte}"

    # FUNÇÃO DO GET(ACESSAR) E SETTER(MODIFICAR) PARA OS ATRIBUTOS PRIVADOS
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
        self.__peso = peso

    # CRIAÇÃO DO PROPERTY
    @property
    def nome(self):
        return self.__nome

    # CRIAÇÃO DO PROPERTY SETTER
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # FUNÇÃO CRIAR NOME DO UNICÓRNIO
    def criar_nome(self):
        nome = input("Digite o nome do seu unicórnio: ")
        self.__nome = nome

    # FUNÇÃO VOAR
    def voar(self):
        while True:
            peso = float(input("Digite o peso do unicórnio: "))
            self.__peso = peso
            if self.__peso > 600 or self.__peso < 100:
                print("Valor Inválido. Digite um valor entre 100 e 600 kg!")
            else:
                velocidade = self.__peso * 0.4
                self.velocidade = velocidade
                print(f"{self.getNome()}, você pode voar até {self.velocidade} km/h!")
                if self.velocidade >= 100:
                    print("Impressionante, você é muito veloz!")
                    break
                elif self.velocidade >= 50:
                    print("Você é capaz de atingir uma velocidade considerável no céu!")
                    break
                else:
                    print("Infelizmente você enfrenta dificuldades ao voar longas distâncias!")
                    break

    # FUNÇÃO POUSAR
    def pousar(self):
        escolha = input(f"{self.getNome()}, você deseja pousar: ").lower()
        if escolha == "sim":
            print("Muito bem, vamos pousar!")
        else:
            print(f"Ok {self.getNome()}, continue aproveitando seu voo!")


# CRIAÇÃO DO OBJETO


unicornio = Unicornio("", "", "", "", "")

# CHAMAR AS FUNÇÕES

unicornio.criar_nome()
print(Unicornio.obter_porte())  # CHAMAR FUNÇÃO DO ATRIBUTO ESTÁTICO
print(Unicornio.gerarIdade())  # CHAMAR FUNÇÃO DO MÉTODO ESTÁTICO
unicornio.voar()
unicornio.pousar()
