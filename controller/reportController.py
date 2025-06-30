from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference
import os

class RelatorioController:
    def gerar_excel(self, dados, nome_arquivo="relatorio_financeiro.xlsx"):
        wb = Workbook()
        ws = wb.active
        ws.title = "Relatório Financeiro"

        ws.append(["Categoria", "Valor (R$)", "Observações"])
        ws["A1"].font = ws["B1"].font = ws["C1"].font = Font(bold=True)

        # Adiciona dados fixos
        ws.append(["Salário", dados.salario, "Fixo mensal"])
        ws.append(["Renda extra", dados.renda_extra, "Outras fontes"])

        linha_gastos_inicio = ws.max_row + 1

        for nome, valor in dados.gastos:
            ws.append([nome, valor, ""])

        linha_gastos_fim = ws.max_row
        ws.append(["Total de gastos", f"=SUM(B{linha_gastos_inicio}:B{linha_gastos_fim})", ""])
        linha_saldo = ws.max_row + 1
        ws.append(["Saldo final", f"=B2+B3-B{linha_saldo - 1}", ""])

        # Gráfico
        chart = BarChart()
        data = Reference(ws, min_col=2, min_row=2, max_row=linha_saldo)
        cats = Reference(ws, min_col=1, min_row=2, max_row=linha_saldo)
        chart.add_data(data, titles_from_data=False)
        chart.set_categories(cats)
        chart.title = "Resumo Financeiro"
        ws.add_chart(chart, "E2")

        wb.save(nome_arquivo)
        return os.path.abspath(nome_arquivo)
