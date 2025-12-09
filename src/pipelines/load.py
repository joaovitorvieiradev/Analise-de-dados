import pandas as pd
from src.db_client import get_db_client

def load_to_supabase (df: pd.DataFrame, table_name: str, key_column: str) -> None:
    if df.empty:
        print("Atenção: O DataFrame '{table_name}' está vazio. Nada a enviar.")
        return
    
    try:
        data = df.to_dict(orient="records")

        client = get_db_client()
        client.table(table_name).upsert(data, on_conflict=key_column).execute()

        print("Sucesso")

    except Exception as e:
        print(f"Erro critico ao enviar para o DB: {e}")
        raise e