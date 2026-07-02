from autoreport.injestion.csv_reader import read_csv


def test_csv_reader():

    df = read_csv("data/sales.csv")

    assert not df.empty

    assert "Product" in df.columns

    assert "Quantity" in df.columns

    assert "Price" in df.columns