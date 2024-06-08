import pandas as pd
from sqlalchemy import create_engine


class GTFSParser:
    DB_URL = "postgresql+psycopg2://postgres:postgres@db/postgres"

    def __init__(self, db_url=None) -> None:
        self.engine = create_engine(db_url or self.DB_URL)

    def parser(self, file_path):
        table_name = file_path.split("/")[-1].split(".")[0]
        df = pd.read_csv(file_path)
        if_exists = "replace" if not self.check_table_exists(table_name) else "append"
        df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
        return table_name

    def check_table_exists(self, table_name):
        return self.engine.dialect.has_table(self.engine, table_name)
