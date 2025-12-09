from src.pipelines.extract import extract_excel
from src.pipelines.transform import process_lojas, clientes, produtos, vendas
from src.pipelines.load import load_to_supabase
import pandas as pd

def run_pipeline():

    print("--- Processando LOJAS ---")
    df_lojas_raw = extract_excel("Cadastro Lojas.xlsx", header=3)
    df_lojas_clean = process_lojas(df_lojas_raw)
    load_to_supabase(df_lojas_clean, "lojas", "store_id")

    print("\n--- Processando CLIENTES ---")
    df_clientes_raw = extract_excel("Cadastro Clientes.xlsx")
    df_clientes_clean = clientes(df_clientes_raw)
    load_to_supabase(df_clientes_clean, "clientes", "client_id")

    print("\n--- Processando PRODUTOS ---")
    df_prod_raw = extract_excel("Cadastro Produto.xlsx")
    df_prod_clean = produtos(df_prod_raw)
    load_to_supabase(df_prod_clean, "produtos", "product_id")

    print("\n--- Processando VENDAS (Concatenação) ---")
    df_22 = extract_excel("Base Vendas - 2022.xlsx")
    df_23 = extract_excel("Base Vendas - 2023.xlsx")
    df_24 = extract_excel("Base Vendas - 2024.xlsx")

    df_vendas_raw = pd.concat([df_22, df_23, df_24], ignore_index=True)
    df_vendas_clean = vendas(df_vendas_raw)
    load_to_supabase(df_vendas_clean, "vendas", "sale_date")

if __name__ == "__main__":
    run_pipeline()