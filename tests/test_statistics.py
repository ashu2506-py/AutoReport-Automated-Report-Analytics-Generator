from autoreport.injestion.csv_reader import read_csv
from autoreport.analysis.statistics import generate_statistics


def test_statistics():

    df = read_csv("data/sales.csv")

    stats = generate_statistics(df)

    assert "shape" in stats

    assert "summary" in stats

    assert stats["shape"][0] > 0