import pandas as pd

def lojas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    rename_map = {
        "Id Loja": "store_id",
        "Cidade": "city",
        "Tipo Loja": "store_type"
    }

    df = df.rename(columns=rename_map)
    df["manager_name"] = df["Nome Gerente"].str.cat(df["Sobrenome Gerente"], sep= ' ')
    df = df.drop(columns=["Nome Gerente", "Sobrenome Gerente"])

    df[["country", "continent"]] = df["Localidade"].str.split(" - ", expand=True)

    final_cols = ["store_id", "city", "country", "continent", "manager_name"]
    return df[final_cols]


def clientes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    rename_map = {
        "Id Cliente": "client_id",
        "Nome Completo": "name",
        "Genero": "gender",
        "Data de Nacimento": "birth"
    }

    df = df.rename(columns=rename_map)
    df["gender"] = df["gender"].replace("F","Feminino").replace("M", "Masculino")

    final_cols = ["client_id", "name", "gender", "birth"]
    return df[final_cols]


def produtos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    rename_map =  {
        "Id Produto": "product_id",
        "Nome Produto": "product_name",
        "Categoria": "category",
        "Marca": "mark",
        "Preço Unit.": "unit_price",
        "Custo Unit.": "unit_cost"
    }

    df = df.rename(columns=rename_map)
    df["unit_price"] = df["unit_price"].str.replace(",",".").astype(float)
    df["unit_cost"] = df["unit_cost"].str.replace(",",".").astype(float)
    df["profit"] = df["unit_price"] - df["unit_cost"]

    final_cols = ["product_id", "product_name", "category", "mark", "unit_price", "unit_cost", "profit"]
    return df[final_cols]


def vendas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    rename_map = {
        "Data Venda": "sale_date",
        "Id Loja": "store_id",
        "Id Produto": "product_id",
        "Id Cliente": "client_id",
        "Qtd. Vendida": "quantity_sold",
        "Qtd. Devolvida": "quantity_returned",
        "Preco Unitario": "unit_price",
    }

    df = df.rename(columns=rename_map)
    df["sale_date"] = pd.to_datetime(df["sale_date"], dayfirst=True)
    df["unit_price"] = df["unit_price"].str.replace(",",".").astype(float)
    df["total_amount"] = df["quantity_sold"] * df["unit_price"]

    final_cols = ["sale_date", "store_id", "product_id", "client_id", "quantity_sold", "quantity_returned", "unit_price", "total_amount"]
    return df[final_cols]

