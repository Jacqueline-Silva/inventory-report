import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type_report: str):
        file = Inventory.reader_file(path)
        if type_report == "simples":
            return SimpleReport.generate(file)
        if type_report == "completo":
            return CompleteReport.generate(file)

    def reader_file(path):
        with open(path) as file:
            content = file.read()
            if ".csv" in path:
                # lista = list(csv.DictReader(file))
                # print(f'\n --- reader in CSV (lista) ---> {lista}\n')
                return Inventory.csv_reader(path)
            if ".json" in path:
                return json.loads(content)
            if ".xml" in path:
                dict = xmltodict.parse(content)
                return list(dict["dataset"]["record"])

    def csv_reader(path):
        with open(path) as file:
            content = list(csv.DictReader(file))
            return content
