from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    def generate(list_inventory):
        return (
            f"{SimpleReport.generate(list_inventory)}\n"
            "Produtos estocados por empresa:\n"
            f"{CompleteReport.inventory_per_company(list_inventory)}"
        )

    def inventory_per_company(list_inventory):
        list = [company["nome_da_empresa"] for company in list_inventory]
        counter_companies = Counter(list)
        more_products = counter_companies.most_common()
        str_report = ""
        for inventory in more_products:
            str_report += f"- {inventory[0]}: {inventory[1]}\n"
        return str_report
