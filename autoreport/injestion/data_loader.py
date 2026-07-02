import os

from .csv_reader import read_csv
from .excel_reader import read_excel
from .json_reader import read_json
from .sqlite_reader import read_sqlite


def load_data(file, table=None):

    extension = os.path.splitext(file)[1].lower()

    if extension == ".csv":
        return read_csv(file)

    elif extension in [".xlsx", ".xls"]:
        return read_excel(file)

    elif extension == ".json":
        return read_json(file)

    elif extension == ".db":

        if table is None:
            raise ValueError("Table name required for SQLite.")

        return read_sqlite(file, table)

    else:
        raise ValueError("Unsupported file format.")