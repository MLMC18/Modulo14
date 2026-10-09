from abc import ABC, abstractmethod

class Quarto(ABC):

    def __init__(self, numero, preco_diaria):
        self.numero = numero
        self.preco_diaria = preco_diaria
        self.ocupado = False

    @property
    @abstractmethod
    def ocupar(self):
        pass
    
    @property
    @abstractmethod
    def libertar(self):
        pass
    
    @abstractmethod 
    def mostrar_informacoes(self): 
        pass

    @property
    @abstractmethod
    def preco_diaria(self):
        pass