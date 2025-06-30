def coletar_dados_usuario():
    print("=== Relatório Financeiro ===")
    salario = float(input("Salário mensal: R$ "))
    renda_extra = float(input("Renda extra: R$ "))
    qtd_gastos = int(input("Quantos tipos de gastos? "))

    gastos = []
    for i in range(qtd_gastos):
        nome = input(f"Nome do gasto #{i+1}: ")
        valor = float(input(f"Valor de '{nome}': R$ "))
        gastos.append((nome, valor))

    return salario, renda_extra, gastos
