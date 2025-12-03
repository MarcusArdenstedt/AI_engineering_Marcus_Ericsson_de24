from pathlib import Path
import duckdb


DATA_PATH = Path(__file__).parent/"data"


def query_Duckdb(sql_code: str, parameters = None):
    with duckdb.connect(DATA_PATH/ "restaurant.duckdb") as conn:
        cursor = conn.execute(sql_code, parameters= parameters)
        
        if sql_code.strip().lower().startswith(("select", "from", "desc", "pragma", "with")):
            return cursor.df()
        
        



