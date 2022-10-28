from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list_inventory):
        manufacturing = SimpleReport.first_product_manufactured(list_inventory)
        validity = SimpleReport.expiration_date(list_inventory)
        company = SimpleReport.company_more_products(list_inventory)
        return (
            f"Data de fabricação mais antiga: {manufacturing}\n"
            f"Data de validade mais próxima: {validity}\n"
            f"Empresa com mais produtos: {company}"
        )

    def first_product_manufactured(list_inventory):
        manufacturing = [date["data_de_fabricacao"] for date in list_inventory]
        return min(manufacturing)

    def expiration_date(list_inventory):
        validity = [date["data_de_validade"] for date in list_inventory]
        return min(validity)

    def company_more_products(list_inventory):
        list = [company["nome_da_empresa"] for company in list_inventory]
        counter_companies = Counter(list)
        more_products = counter_companies.most_common()
        return more_products[0][0]
