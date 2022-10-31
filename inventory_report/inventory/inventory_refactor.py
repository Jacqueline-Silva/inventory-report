from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, type_report: str):
        # via composição: ex: InventoryRefactor(CsvImporter)
        self.data += self.importer.import_data(path)

        if type_report == "simples":
            return SimpleReport.generate(self.data)
        if type_report == "completo":
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
