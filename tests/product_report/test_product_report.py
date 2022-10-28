from inventory_report.inventory.product import Product
from tests.product.test_product import phrase, mock_product


def test_relatorio_produto():
    product = Product(
        mock_product["id"],
        mock_product["produto"],
        mock_product["empresa"],
        mock_product["fabricacao"],
        mock_product["validade"],
        mock_product["n_serie"],
        mock_product["inst"],
    )

    assert product.__repr__() == phrase
