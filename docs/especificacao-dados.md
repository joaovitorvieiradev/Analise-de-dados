# Especificação de Dados e Mapeamento

## Padrões Gerais
* **Nomenclatura no Banco:** Snake Case (`nome_do_campo`).
* **Moeda:** Decimal/Float (Não usar Money proprietário).
* **Datas:** ISO 8601 (YYYY-MM-DD).

## 1. Tabela: `dim_clientes` (Origem: Cadastro Clientes)
```
| Coluna Excel | Coluna Banco | Tipo SQL | Obrigatório | Obs |
| :--- | :--- | :--- | :--- | :--- |
| ID Cliente | `client_id` | INT (PK) | Sim | |
| Primeiro Nome | `first_name` | TEXT | Sim | |
| Sobrenome | `last_name` | TEXT | Sim | |
| Email | `email` | TEXT | Não | Validar formato de e-mail |
| Genero | `gender` | CHAR(1) | Não | |
```

## 2. Tabela: `dim_lojas` (Origem: Cadastro Lojas)
```
| Coluna Excel | Coluna Banco | Tipo SQL | Obrigatório | Obs |
| :--- | :--- | :--- | :--- | :--- |
| ID Loja | `store_id` | INT (PK) | Sim | |
| Nome da Loja | `store_name` | TEXT | Sim | |
| Quantidade Colaboradores | `employee_count` | INT | Não | |
| País | `country` | TEXT | Não | Extraído de "Localidade" |
```
## 3. Tabela: `dim_produtos` (Origem: Cadastro Produto)
```
| Coluna Excel | Coluna Banco | Tipo SQL | Obrigatório | Obs |
| :--- | :--- | :--- | :--- | :--- |
| ID Produto | `product_id` | INT (PK) | Sim | |
| Nome do Produto | `product_name` | TEXT | Sim | |
| Custo Unitario | `unit_cost` | DECIMAL(10,2)| Sim | Limpar "R$" e "," |
```
## 4. Tabela: `fact_vendas` (Origem: Base Vendas)
```
| Coluna Excel | Coluna Banco | Tipo SQL | Obrigatório | Obs |
| :--- | :--- | :--- | :--- | :--- |
| ID Venda | `sale_id` | TEXT (PK) | Sim | Cuidado com duplicatas |
| Data da Venda | `sale_date` | DATE | Sim | |
| ID Loja | `store_id` | INT (FK) | Sim | |
| ID Produto | `product_id` | INT (FK) | Sim | |
| ID Cliente | `client_id` | INT (FK) | Sim | |
| Qtd Vendida | `quantity` | INT | Sim | |
| Preco Unitario | `unit_price` | DECIMAL(10,2)| Sim | Tratamento crítico de string |
```