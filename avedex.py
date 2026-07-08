import unicodedata


def exibir_linha():
    print("=" * 50)


def exibir_menu():
    print()
    exibir_linha()
    print("AVEDEX - MENU PRINCIPAL")
    exibir_linha()
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Listar aves")
    print("3 - Ver detalhes de uma ave (por código)")
    print("4 - Buscar aves (busca avançada)")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")


def listar_aves(catalogo):
    print()
    exibir_linha()
    print("AVES CADASTRADAS")
    exibir_linha()
    for ave in catalogo:
        print(f"{ave['codigo']} - {ave['nome_popular']}")


def buscar_ave_por_codigo(catalogo, codigo_procurado):
    for ave in catalogo:
        if ave["codigo"] == codigo_procurado:
            return ave
    return None


# 🔧 NORMALIZAÇÃO DE TEXTO
def normalizar_texto(texto):
    texto = str(texto)
    texto = texto.lower().strip()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


# 🔍 NOVA BUSCA MULTICAMPOS (ETAPA 4)
def buscar_aves(catalogo, termo_busca):
    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in catalogo:

        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        texto_busca = " ".join(campos_busca)
        texto_busca = normalizar_texto(texto_busca)

        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_detalhes(ave):
    print()
    exibir_linha()
    print("DETALHES DA AVE")
    exibir_linha()
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'N/A')}")
    print(f"Família: {ave.get('familia', 'N/A')}")
    print(f"Dieta: {ave.get('dieta_tipo', 'N/A')}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave['curiosidade']}")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves.")
    print("O projeto evolui durante a disciplina de Boas Práticas.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


catalogo_aves = [
    {
        "codigo": "1",
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Insetívora e frugívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto lembra a expressão bem-te-vi."
    },
    {
        "codigo": "2",
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos, áreas abertas e ambientes rurais",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    },
    {
        "codigo": "3",
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "Constrói um ninho de barro característico."
    },
    {
        "codigo": "4",
        "nome_popular": "Arara-azul",
        "nome_cientifico": "Anodorhynchus hyacinthinus",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Frugívora",
        "habitat": "Florestas, cerrado e Pantanal",
        "alimentacao": "Frutos, sementes e castanhas",
        "curiosidade": "É a maior espécie de arara do mundo."
    },
    {
        "codigo": "5",
        "nome_popular": "Coruja-buraqueira",
        "nome_cientifico": "Athene cunicularia",
        "ordem": "Strigiformes",
        "familia": "Strigidae",
        "dieta_tipo": "Carnívora",
        "habitat": "Campos abertos e áreas urbanas",
        "alimentacao": "Insetos e pequenos vertebrados",
        "curiosidade": "Vive em buracos no solo e é ativa durante o dia."
    }
]

print("=" * 50)
print(" AVEDEX")
print("=" * 50)

nome_usuario = input("Digite seu nome: ").strip()

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()
    opcao_menu = input("Escolha uma opção: ").strip()
    print()

    if opcao_menu == "1":
        mostrar_boas_vindas(nome_usuario)

    elif opcao_menu == "2":
        listar_aves(catalogo_aves)

    elif opcao_menu == "3":
        listar_aves(catalogo_aves)

        codigo_escolhido = input("\nDigite o código da ave: ").strip()

        ave_encontrada = buscar_ave_por_codigo(catalogo_aves, codigo_escolhido)

        if ave_encontrada:
            exibir_detalhes(ave_encontrada)
        else:
            print("Ave não encontrada.")

    elif opcao_menu == "4":
        termo = input("Digite sua busca: ").strip()

        resultados = buscar_aves(catalogo_aves, termo)

        if resultados:
            print("\nAVES ENCONTRADAS:")
            for ave in resultados:
                print(f"{ave['codigo']} - {ave['nome_popular']}")
        else:
            print("Nenhuma ave encontrada.")

    elif opcao_menu == "5":
        mostrar_sobre()

    elif opcao_menu == "0":
        print("Encerrando a AveDex.")
        print(f"Até logo, {nome_usuario}!")

    else:
        print("Opção inválida.")

    if opcao_menu != "0":
        pausar()