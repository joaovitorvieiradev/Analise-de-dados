# ADR 001: Definição da Arquitetura e Stack Tecnológica

## Status
Aceito

## Contexto
O projeto necessita processar múltiplas planilhas Excel (Vendas, Clientes, Produtos, Lojas) disponibilizadas em rede corporativa diariamente. Os dados contêm inconsistências de tipagem (ex: moedas formatadas como texto) e precisam ser consolidados em um Banco de Dados Relacional para análise de BI.

## Decisão
Decidimos utilizar a seguinte stack:
1. **Linguagem:** Python 3.10+ (Pela robustez em tipagem e bibliotecas de dados).
2. **ETL:** Pandas + Openpyxl (Processamento em memória).
3. **Validação:** Pydantic (Para garantir schema strict antes da inserção no banco).
4. **Banco de Dados:** Supabase (PostgreSQL) na nuvem.
5. **Estratégia de Carga:** Truncate & Load (Substituição total diária).

## Justificativa
* **Supabase:** Oferece PostgreSQL gerenciado com API pronta, eliminando custo de manutenção de servidor de banco local.
* **Truncate & Load:** Como os arquivos de origem são sobrescritos e não possuem chave incremental confiável ("delta"), a substituição total é a única forma de garantir consistência e evitar duplicidade de registros corrigidos retroativamente.
* **Pydantic:** O Pandas infere tipos incorretamente em colunas sujas (ex: "2.200,00" virando string). O Pydantic força a validação na entrada.

## Consequências
* **Positivo:** Integridade de dados garantida; Banco sempre reflete exatamente a planilha atual.
* **Negativo:** Perda de histórico se a planilha de origem for limpa pelo usuário (mitigado por backups ou tabelas de histórico.).