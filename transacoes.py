from dataclasses import dataclass
from categorias import Categorias


@dataclass
class Transacoes:
    valor:float
    nome:str
    categoria: Categorias


    def exibirDados(self):
        print(f"VALOR DA TRANSAÇÃO: {self.valor} || NOME DA TRANSAÇÃO: {self.nome} || CATEGORIA DA TRANSAÇÃO: {self.categoria}")
