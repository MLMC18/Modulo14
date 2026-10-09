from pessoa import Pessoa
from quarto import Quarto

lista_hospedes = {}
lista_funcionarios = []
lista_quartos = {}


class Funcionario(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self._salario = salario

    @property
    def defenirnome(self):
        return self.nome 

    @defenirnome.setter
    def defenirnome(self, nome):
        self.nome = nome
    
    @property
    def defeniridade(self):
        return self.idade

    @defeniridade.setter
    def defeniridade(self, idade):
        self.idade = idade
    
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Salário: {self._salario}")
        print("-"*4 + "\n")

class Hospede(Pessoa):

    def __init__(self, nome, idade, dias_estadia):
        super().__init__(nome, idade)
        self.dias_estadia = dias_estadia
        self.quarto = None

    def atribuir_quarto(self, quarto):
        self.quarto = quarto

    def calcular_conta(self):
        if self.quarto:
            return self.dias_estadia * self.quarto.preco_por_noite
        return 0

    def checkout(self):
        if self.quarto:
            self.quarto.libertar()
            self.quarto = None

    @property
    def defenirnome(self):
        return self.nome 

    @defenirnome.setter
    def defenirnome(self, nome):
        self.nome = nome
    
    @property
    def defeniridade(self):
        return self.idade

    @defeniridade.setter
    def defeniridade(self, idade):
        self.idade = idade

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Dias: {self.dias_estadia}")
        print("-"*4 + "\n")


class Gerente(Funcionario):

    def __init__(self, nome, idade, salario, bonus):
        super().__init__(nome, idade, salario)
        self._bonus = bonus

    def mostrar_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Salário:", self._salario)
        print("Bónus:", self._bonus)

    def gerar_relatorio(self, funcionarios):
        for funcionario in funcionarios:
            funcionario.mostrar_informacoes()

class Recepcionista(Funcionario):

    def __init__(self, nome, idade, salario, turno):
        super().__init__(nome, idade, salario)
        self.turno = turno

    def registar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)

    def listar_hospedes(self, lista_hospedes):
        for hospede in lista_hospedes:
            hospede.mostrar_informacoes()

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Turno: {self.turno}")


class TecnicoManutencao(Funcionario):

    def __init__(self, nome, idade, salario, especialidade):
        super().__init__(nome, idade, salario)
        self._especialidade = especialidade

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, valor):
        self._especialidade = valor

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Especialidade: {self.especialidade}")

class TecnicoRecepcao(TecnicoManutencao,Recepcionista):
    
    def __init__(self, nome, id_funcionario, salario, setor, especialidade):
        TecnicoManutencao.__init__(self, nome, id_funcionario, salario, setor, especialidade)
        Recepcionista.__init__(self, nome, id_funcionario, salario, setor)
        self.nome = nome
        self.id_funcionario
        self._salario = salario
        self.setor = setor
        self.especialidade = especialidade

    def registar_hospede(self, nome_hospede):
        print(f"Hospede Registrado! Nome: {nome_hospede}")
    
    def registar_reparo(self, descrição):
        print(f"Reparo Registrado! Descrição:{descrição}")

    def mostrar_informações(self):
        TecnicoManutencao.mostrar_info(self)
        Recepcionista.mostrar_info(self)



while True:
    print("\nMenu")
    print("1 - Registar hóspede")
    print("2 - Listar hóspedes")
    print("3 - Registar funcionário")
    print("4 - Listar funcionários")
    print("5 - Registar reparo")
    print("6 - Registar quarto")
    print("7 - Check in")
    print("8 - Check out")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do hóspede: ")
        idade = int(input("Idade: "))
        dias = int(input("Dias de estadia: "))

        hospede = Hospede(nome, idade, dias)
        lista_hospedes.append(hospede)

        print("Hóspede registado com sucesso!")

    elif opcao == "2":
        if len(lista_hospedes) > 0:
            for hospede in lista_hospedes:
                hospede.mostrar_informacoes()
        else:
            print("Não existe nenhum hospede")

    elif opcao == "3":
        nome = input("Nome do funcionário: ")
        idade = int(input("Idade: "))
        salario = float(input("Salário: "))

    
        funcionario = Funcionario(nome, idade, salario)
        lista_funcionarios.append(funcionario)

        print("Funcionário registado com sucesso!")

    elif opcao == "4":
        if len(lista_funcionarios) > 0:
            for funcionario in lista_funcionarios:
                funcionario.mostrar_informacoes()
        else:
            print("Não existe nenhum funcionario")

    elif opcao == "5":
        nome = input("Nome do Técnico de Manutenção: ")
        idade = int(input("Idade: "))
        salario = float(input("Salário: "))
        especialidade = input("Especialidade do Funcionario: ")

    
        tecnico = TecnicoManutencao(nome, idade, salario, especialidade)
        lista_funcionarios.append(tecnico)

        print("Funcionário registado com sucesso!")

    
    elif opcao == "6":
        # Criar automaticamente os quartos de 0 a 50
        for numero in range(51):
            if str(numero) not in lista_quartos:
                lista_quartos[str(numero)] = [False, "", 0, 0.0]

        numero = input("Qual é o número do quarto que queres registar (0-50)? ")

        if numero in lista_quartos:
            print("Escolhe o preço por noite:")
            print("1 - 50 euros")
            print("2 - 100 euros")

            escolha = input("Opção: ")

            if escolha == "1":
                preco = 50
            elif escolha == "2":
                preco = 100
            else:
                print("Opção inválida!")
                continue

            lista_quartos[numero][3] = preco

            print(f"Quarto {numero} registado com sucesso!")
            print(f"Preço por noite: {preco} euros")

        if numero not in lista_quartos:
            print("Quarto inválido! Escolhe um número de 0 a 50.")

    elif opcao == "7":
        nome = input("Nome do hóspede: ")
        idade = int(input("Idade: "))
        dias = int(input("Dias de estadia: "))

        if nome not in lista_hospedes:
            hospede = Hospede(nome, idade, dias)
            lista_hospedes[nome] = hospede
        else:
            hospede = lista_hospedes[nome]
            hospede.dias_estadia = dias

        print("Quartos disponíveis:")

        for numero, dados in lista_quartos.items():
            if dados[0] == False:
                print(f"Quarto {numero} - {dados[3]} euros por noite")

        numero = input("Escolhe o número do quarto: ")

        if numero in lista_quartos:
            if lista_quartos[numero][0] == False:
                lista_quartos[numero][0] = True
                lista_quartos[numero][1] = nome
                lista_quartos[numero][2] = dias

                hospede.atribuir_quarto(numero)

                print("Check-in realizado com sucesso!")
                print(f"Hóspede: {nome}")
                print(f"Quarto: {numero}")
                print(f"Dias: {dias}")
            else:
                print("Este quarto já está ocupado!")

        if numero not in lista_quartos:
            print("Esse quarto não existe!")

    elif opcao == "8":
        nome = input("Nome do hóspede: ")
        quarto_encontrado = False

        for numero, dados in lista_quartos.items():
            if dados[1] == nome and dados[0] == True:
                dias = dados[2]
                preco = dados[3]
                total = dias * preco

                print(f"Hóspede: {nome}")
                print(f"Quarto: {numero}")
                print(f"Dias de estadia: {dias}")
                print(f"Preço por noite: {preco} euros")
                print(f"Total a pagar: {total} euros")

                dados[0] = False
                dados[1] = ""
                dados[2] = 0

                if nome in lista_hospedes:
                    del lista_hospedes[nome]

                print("Check-out realizado com sucesso!")
                quarto_encontrado = True
                break

        if quarto_encontrado == False:
            print("Hóspede não encontrado ou sem quarto atribuído!")

    elif opcao == "9":
        print("A sair do programa...")
        break