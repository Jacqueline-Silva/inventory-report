from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    list_products = [
        {
            "id": 1,
            "nome_do_produto": "CADEIRA 1",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-03",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 2,
            "nome_do_produto": "CADEIRA 2",
            "nome_da_empresa": "FN",
            "data_de_fabricacao": "2021-04-04",
            "data_de_validade": "2024-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
    ]

    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[36m"
    end = "\033[0m"

    simple_report = ColoredReport(SimpleReport)
    simple_report_result = simple_report.generate(list_products)

    s_report = (
        f"{green}Data de fabricação mais antiga:{end} {blue}2021-04-04{end}\n"
        f"{green}Data de validade mais próxima:{end} {blue}2023-02-09{end}\n"
        f"{green}Empresa com mais produtos:{end} {red}Forces of Nature{end}"
    )

    assert simple_report_result == s_report
