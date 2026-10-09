from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    @abstractmethod
    def defenirnome(self):
       pass

    @defenirnome.setter
    @abstractmethod
    def defenirnome(self, nome):
        pass

    @property
    @abstractmethod
    def defeniridade(self):
        pass
    
    @defeniridade.setter
    @abstractmethod
    def defeniridade(self, idade):
        pass

    @abstractmethod
    def mostrar_informacoes(self):
        pass