class DadosFinanceiros:
    def __init__(self, salario, renda_extra, gastos):
        self.salario = salario
        self.renda_extra = renda_extra
        self.gastos = gastos  # Lista de tuplas [(nome, valor), ...]

    def total_gastos(self):
        return sum(valor for _, valor in self.gastos)

    def saldo_final(self):
        return self.salario + self.renda_extra - self.total_gastos()
