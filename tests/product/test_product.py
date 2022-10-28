from inventory_report.inventory.product import Product

mock_product = {
    "id": 1,
    "produto": "Chocolate em barra sabor Cookie",
    "empresa": "Nestlé",
    "fabricacao": "2021-05-21",
    "validade": "2022-05-21",
    "n_serie": "1345678522",
    "inst": "em local fresco e longe do sol",
}

phrase = (
    "O produto Chocolate em barra sabor Cookie"
    " fabricado em 2021-05-21"
    " por Nestlé com validade"
    " até 2022-05-21"
    " precisa ser armazenado em local fresco e longe do sol."
)


def test_cria_produto():
    product = Product(
        mock_product["id"],
        mock_product["produto"],
        mock_product["empresa"],
        mock_product["fabricacao"],
        mock_product["validade"],
        mock_product["n_serie"],
        mock_product["inst"],
    )

    assert product.id == mock_product["id"]
    assert product.nome_do_produto == mock_product["produto"]
    assert product.nome_da_empresa == mock_product["empresa"]
    assert product.data_de_fabricacao == mock_product["fabricacao"]
    assert product.data_de_validade == mock_product["validade"]
    assert product.numero_de_serie == mock_product["n_serie"]
    assert product.instrucoes_de_armazenamento == mock_product["inst"]

    assert product.__repr__() == phrase
