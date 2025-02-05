from categorias import Categorias
from transacoes import Transacoes


LISTA__TRANSACOES = []
LISTA__CATEGORIAS = []




def cadastrar_transacoes(valor, nome, categoria):
    nova_transacao = Transacoes(
        valor=valor,
        nome=nome,
        categoria=categoria
    )
    LISTA__TRANSACOES.append(nova_transacao)

    return nova_transacao



def cadastrar_categoria(nome):
    nova_categoria = Categorias(
        nome=nome
    )
    LISTA__CATEGORIAS.append(nova_categoria)

    return nova_categoria



def valor_total():
    total = 0

    for i in LISTA__TRANSACOES:
        total += i.valor

    return total