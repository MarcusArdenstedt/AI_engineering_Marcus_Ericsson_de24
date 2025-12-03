from utils import query_Duckdb

query_Duckdb(
    """
            CREATE TABLE IF NOT EXISTS restaurant (
            name STRING,
            type_of_food TEXT,
            pricing_level TINYINT,
            rating float,
            short_description TEXT,
            opening_hours time,
            latitude DOUBLE,
            longitude DOUBLE
            )
        """
)
