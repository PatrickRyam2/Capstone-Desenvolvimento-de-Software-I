import json
import os
import vendedores

ARQUIVO = "vendas.json"


def carregar_vendas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


vendas = carregar_vendas()
def selecionar_vendedor():
    vendedores_cadastrados = vendedores.vendedores

    if not vendedores_cadastrados:
        print("Nenhum vendedor cadastrado.")
        return None

    print("\n===== VENDEDORES DISPONÍVEIS =====")

    for vendedor in vendedores_cadastrados:
        print(f"ID: {vendedor['id']} | Nome: {vendedor['nome']}")

    id_escolhido = int(input("\nDigite o ID do vendedor: "))

    for vendedor in vendedores_cadastrados:
        if vendedor["id"] == id_escolhido:
            return vendedor

    print("Vendedor não encontrado.")
    return None


def salvar_vendas():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(vendas, arquivo, indent=4, ensure_ascii=False)


def gerar_id_venda():
    return max([v["id_venda"] for v in vendas], default=0) + 1


class Venda:
    def __init__(self, cliente, vendedor, veiculo, preco, data, forma_pagamento):
        self.id_venda = gerar_id_venda()
        self.cliente = cliente
        self.vendedor = vendedor
        self.veiculo = veiculo
        self.preco = preco
        self.data = data
        self.forma_pagamento = forma_pagamento
        
        

    def calcular_comissao(self):
        percentual = self.vendedor["percentual_comissao"]
        comissao = self.preco * percentual / 100
        return comissao

    def salvar(self):
        registro = {
            "id_venda": self.id_venda,
            "cliente": self.cliente,
            "vendedor": self.vendedor["nome"],
            "veiculo": self.veiculo,
            "preco": self.preco,
            "data": self.data,
            "forma_pagamento": self.forma_pagamento,
            "comissao": self.calcular_comissao()
        }

        vendas.append(registro)
        salvar_vendas()
def registrar_venda():
    print("\n===== REGISTRO DE VENDA =====")

    vendedor_escolhido = selecionar_vendedor()

    if not vendedor_escolhido:
        return

    cliente = input("\nNome do cliente: ")
    veiculo = input("Modelo do veículo: ")
    preco = float(input("Preço da venda: ").replace(",", "."))
    data = input("Data da venda: ")
    forma_pagamento = input("Forma de pagamento: ")

    venda = Venda(
        cliente,
        vendedor_escolhido,
        veiculo,
        preco,
        data,
        forma_pagamento
    )

    venda.salvar()

    print("\nVenda registrada com sucesso!")
    print("ID da venda:", venda.id_venda)
    print("Comissão:", venda.calcular_comissao())


if __name__ == "__main__":
    registrar_venda()

    
    
