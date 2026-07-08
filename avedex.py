import unicodedata


def exibir_linha():
    print("=" * 50)


def exibir_menu():
    print()
    exibir_linha()
    print("AVEDEX - MENU PRINCIPAL")
    exibir_linha()
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Sobre a AveDex")
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


def selecionar_ave_por_id(catalogo_aves):
    codigo = input("Digite o código da ave: ").strip()
    ave = buscar_ave_por_codigo(catalogo_aves, codigo)

    if ave:
        exibir_detalhes(ave)
    else:
        print("Ave não encontrada.")


def normalizar_texto(texto):
    texto = str(texto)
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )
    return texto


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

        texto_busca = normalizar_texto(" ".join(campos_busca))

        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_resultados_busca(resultados):
    print()
    exibir_linha()
    print("RESULTADOS DA BUSCA")
    exibir_linha()

    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(
                f"{ave['codigo']} - {ave['nome_popular']} "
                f"({ave.get('familia', 'N/A')}, {ave.get('dieta_tipo', 'N/A')})"
            )


def tela_busca(catalogo):
    termo = input("Digite parte do nome, família, ordem ou dieta: ").strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    resultados = buscar_aves(catalogo, termo)

    exibir_resultados_busca(resultados)

    if len(resultados) > 0:
        escolha = input("\nDigite o código da ave para ver detalhes ou ENTER para voltar: ").strip()

        if escolha != "":
            ave = buscar_ave_por_codigo(resultados, escolha)

            if ave is None:
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes(ave)


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
        "curiosidade": "Seu canto lembra a expressão bem-te-vi.",
        "comprimento_cm": 23,
        "peso_g": 68,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1
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
        "curiosidade": "Possui canto forte e melodioso.",
        "comprimento_cm": 13,
        "peso_g": 13,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1
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
        "curiosidade": "Constrói um ninho de barro característico.",
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1
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
        "curiosidade": "É a maior espécie de arara do mundo.",
        "comprimento_cm": 100,
        "peso_g": 1400,
        "status_conservacao": "Vulnerável",
        "indice_conservacao": 3
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
        "curiosidade": "Vive em buracos no solo e é ativa durante o dia.",
        "comprimento_cm": 24,
        "peso_g": 180,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1
    },
    {
        "codigo": "6",
        "nome_popular": "Sabiá-laranjeira",
        "nome_cientifico": "Turdus rufiventris",
        "ordem": "Passeriformes",
        "familia": "Turdidae",
        "dieta_tipo": "Onívora",
        "habitat": "Florestas, áreas urbanas, jardins e parques",
        "alimentacao": "Frutas, insetos e pequenos invertebrados",
        "curiosidade": "É considerado o pássaro símbolo do Brasil.",
        "comprimento_cm": 25,
        "peso_g": 70,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1
    },
    {
        "codigo": "7",
        "nome_popular": "Tico-tico",
        "nome_cientifico": "Zonotrichia capensis",
        "ordem": "Passeriformes",
        "familia": "Passerellidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos, jardins, áreas abertas e cidades",
        "alimentacao": "Sementes, insetos e pequenos frutos",
        "curiosidade": "Muito comum no Brasil e conhecido pelo canto repetitivo.",
        "comprimento_cm": 15,
        "peso_g": 24,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1
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
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        mostrar_sobre()

    elif opcao_menu == "0":
        print("Encerrando a AveDex.")
        print(f"Até logo, {nome_usuario}!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3 ou 4.")

    if opcao_menu != "0":
        pausar()