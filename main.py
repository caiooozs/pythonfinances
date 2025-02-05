from dataclasses import dataclass
from categorias import Categorias
from transacoes import Transacoes
from utilitarios import(cadastrar_transacoes,cadastrar_categoria,valor_total)




fixa = cadastrar_categoria("Conta Fixa")
futil = cadastrar_categoria("Conta Fixa")
viagem = cadastrar_categoria("Conta Fixa")




cadastrar_transacoes(valor=-1,nome="jantar",categoria=futil)
cadastrar_transacoes(valor=+1,nome="mesada",categoria=futil)
cadastrar_transacoes(valor=-1,nome="luz",categoria=fixa)


total = valor_total()

print(total)
