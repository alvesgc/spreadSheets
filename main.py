from model.financeData import DadosFinanceiros
from controller.reportController import RelatorioController
from view.interface import coletar_dados_usuario

def main():
    salario, renda_extra, gastos = coletar_dados_usuario()
    dados = DadosFinanceiros(salario, renda_extra, gastos)

    controller = RelatorioController()
    caminho_arquivo = controller.gerar_excel(dados)

    print(f"\n✅ Relatório gerado com sucesso: {caminho_arquivo}")

if __name__ == "__main__":
    main()
