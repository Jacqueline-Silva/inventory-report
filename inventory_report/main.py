import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    importers_file = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter
    }
    try:
        # ex: inventory_report, '/arq.csv', 'simples'
        path, type_report = sys.argv[1:]
        importer = path.split('.')[1]
        file = InventoryRefactor(importers_file[importer])
        sys.stdout.write(file.import_data(path, type_report))
    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")


# stdout = print
# stderr = exceções
# stdin = input
