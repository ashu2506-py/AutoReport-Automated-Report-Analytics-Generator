from autoreport.injestion.data_loader import load_data


def test_data_loader():

    df = load_data("data/sales.csv")

    assert not df.empty