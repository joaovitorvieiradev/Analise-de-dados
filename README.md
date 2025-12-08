# Projeto BI Corporativo - Pipeline ETL

## 1. Visão Geral
Sistema de extração, transformação e carga (ETL) para consolidar dados de vendas, lojas e produtos em um Data Warehouse no Supabase.

## 2. Objetivo de Negócio
Garantir que a diretoria tenha acesso a dados atualizados diariamente (D-1) sem intervenção manual, eliminando erros de planilhas.

## 3. Origem dos Dados
- **Formato:** Arquivos .xlsx
- **Local:** Rede Corporativa (Simulada em `./data/input`)
- **Frequência:** Diária (Sobrescrita)

## 4. Estratégia de Carga
- Modelo: Truncate & Load (Substituição Total)
- Janela de Execução: 03:00 AM
- Tratamento de Erros: Logs em tabela dedicada e Retries automáticos.