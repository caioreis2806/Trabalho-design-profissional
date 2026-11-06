# ==========================================
# SISTEMA DE CONTROLE DE ESTOQUE
# Integrantes: Caio, David e João
# ==========================================


# ==========================================
# PARTE 1 - CAIO
# Estrutura, cadastro e consulta de produtos
# ==========================================

# Lista responsável por armazenar os produtos.
# Cada produto será representado por um dicionário.
estoque = []


def buscar_produto(codigo):
    # Percorre todos os produtos cadastrados.
    for produto in estoque:

        # Verifica se o código corresponde ao procurado.
        if produto["codigo"] == codigo:
            return produto

    # Retorna None caso não encontre o produto.
    return None


def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")

    # Solicita o código e remove espaços extras.
    codigo = input("Código do produto: ").strip()

    # Impede o cadastro de códigos vazios.
    if not codigo:
        print("O código não pode ficar vazio.")
        return

    # Impede produtos com códigos repetidos.
    if buscar_produto(codigo):
        print("Já existe um produto com esse código!")
        return

    # Solicita o nome do produto.
    nome = input("Nome do produto: ").strip()

    if not nome:
        print("O nome não pode ficar vazio.")
        return

    # Trata possíveis erros na quantidade informada.
    try:
        quantidade = int(input("Quantidade inicial: "))

        # Impede quantidades negativas.
        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
            return

    except ValueError:
        print("Digite uma quantidade válida.")
        return

    # Cria um dicionário com os dados do produto.
    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade
    }

    # Adiciona o dicionário à lista de estoque.
    estoque.append(produto)

    print("Produto cadastrado com sucesso!")


def consultar_estoque():
    print("\n--- ESTOQUE ATUAL ---")

    # Verifica se existem produtos cadastrados.
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    # Exibe o cabeçalho da tabela.
    print(f"{'CÓDIGO':<12} {'PRODUTO':<25} {'QUANTIDADE':<12}")
    print("-" * 49)

    # Percorre a lista e apresenta cada produto.
    for produto in estoque:
        print(
            f"{produto['codigo']:<12} "
            f"{produto['nome']:<25} "
            f"{produto['quantidade']:<12}"
        )

# ==========================================
# PARTE 2 - DAVID
# Entrada e saída de produtos do estoque
# ==========================================

def adicionar_estoque():
    print("\n--- ADICIONAR ESTOQUE ---")

    # Solicita o código do produto.
    codigo = input("Código do produto: ").strip()

    # Localiza o produto usando a função de busca.
    produto = buscar_produto(codigo)

    # Verifica se o produto existe.
    if produto is None:
        print("Produto não encontrado.")
        return

    # Solicita a quantidade que será adicionada.
    try:
        quantidade = int(input("Quantidade para adicionar: "))

        # Aceita apenas valores maiores que zero.
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

    except ValueError:
        print("Quantidade inválida.")
        return

    # Soma a quantidade informada ao estoque atual.
    produto["quantidade"] += quantidade

    print("Estoque atualizado com sucesso!")
    print(f"Quantidade atual: {produto['quantidade']}")


def retirar_estoque():
    print("\n--- RETIRAR PRODUTOS ---")

    # Solicita o código do produto.
    codigo = input("Código do produto: ").strip()

    # Procura o produto na lista.
    produto = buscar_produto(codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    # Solicita a quantidade que será retirada.
    try:
        quantidade = int(input("Quantidade para retirar: "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

    except ValueError:
        print("Quantidade inválida.")
        return

    # Verifica se existe quantidade suficiente.
    if quantidade > produto["quantidade"]:
        print("Estoque insuficiente!")
        print(f"Disponível: {produto['quantidade']}")
        return

    # Subtrai a quantidade retirada do estoque.
    produto["quantidade"] -= quantidade

    print("Retirada realizada com sucesso!")
    print(f"Quantidade restante: {produto['quantidade']}")
