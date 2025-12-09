from pipelines.transform import lojas, clientes, produtos, vendas
from pipelines.extract import extract_excel
import pandas as pd

df_bruto_lojas = extract_excel("Cadastro Lojas.xlsx", header=3)
df_tratado_lojas = lojas(df_bruto_lojas)

df_bruto_clientes = extract_excel("Cadastro Clientes.xlsx")
df_tratado_clientes = clientes(df_bruto_clientes)

df_bruto_produtos = extract_excel("Cadastro Produtos.xlsx")
df_tratado_produtos = produtos(df_bruto_produtos)

df_bruto_vendas_2022 = extract_excel("Base Vendas - 2022")
df_bruto_vendas_2023 = extract_excel("Base Vendas - 2023")
df_bruto_vendas_2024 = extract_excel("Base Vendas - 2024")
df_geral = pd.concat([df_bruto_vendas_2022, df_bruto_vendas_2023, df_bruto_vendas_2024])
df_tratado_vendas = vendas(df_geral)
