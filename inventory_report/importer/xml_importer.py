import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            content = file.read()
            result = xmltodict.parse(content)
            return list(result["dataset"]["record"])
