# Mini Projeto Avaliativo — Análise de Dados com Python

## Objetivo

Este projeto realiza uma Análise Exploratória de Dados (AED) da base Varejo com Python e pandas. O objetivo é identificar problemas de qualidade nos dados, realizar a limpeza necessária, calcular estatísticas descritivas e encontrar padrões de compras.

## Base de dados

A base utilizada é `varejo.csv`, com registros de compras, clientes e produtos do varejo.

A base original pode ser obtida no Kaggle:

https://www.kaggle.com/datasets/namespaiva/base-varejo/data

Para executar o script, salve o arquivo `varejo.csv` na mesma pasta de `miniprojeto_varejo.py`.

## Estrutura do projeto

- `miniprojeto_varejo.py`: script que realiza a leitura, limpeza e análise dos dados.
- `df_limpo.csv`: base gerada após o tratamento dos dados.
- `README.md`: documentação principal do projeto.
- `README_Mateus_Aimi_Analise_de_Dados_T4.md`: instruções simples de execução.

## Tecnologias utilizadas

- Python 3.14
- csv (biblioteca nativa do Python)
- pandas 3.0.5
- Git e GitHub

## Etapas realizadas

1. Leitura estruturada inicial da base `varejo.csv` com `csv.DictReader` e leitura para análise com pandas, usando ponto e vírgula como separador.
2. Remoção de quatro colunas totalmente vazias, criadas pelos separadores extras presentes no arquivo original.
3. Verificação de valores nulos, duplicatas, datas e campos de texto vazios.
4. Remoção de 96.553 linhas totalmente duplicadas.
5. Conversão da coluna `DATA` para o tipo de data.
6. Substituição de registros `#N/D` na coluna `PR_CAT` por `Sem Categoria`.
7. Validação do identificador de compra (`CO_ID`) e do perfil de cada cliente (`CL_ID`).
8. Cálculo das estatísticas de número de filhos por cliente.
9. Criação de agrupamentos por gênero e segmento, e por categoria de produto.
10. Exportação da base tratada como `df_limpo.csv`.

## Principais insights

- Foram removidas 96.553 linhas duplicadas, equivalentes a 11,63% da base original.
- Dos 1.000 clientes únicos, 52,7% não possuem filhos. A média foi de 1,14 filho por cliente.
- O segmento B concentrou 64,12% das compras únicas registradas.
- A categoria ALIMENTOS esteve presente em 98,90% das compras únicas e foi a categoria com mais itens registrados.
- HIGIENE e LIMPEZA também aparecem em grande parte das compras, indicando presença frequente de produtos essenciais.
  
## Limitações e problemas remanescentes

- Foram encontrados 3.228 registros originalmente identificados como `#N/D`, que foram padronizados como `Sem Categoria`.
- A base não possui preço, quantidade vendida ou valor de venda. Portanto, não é possível analisar faturamento.

## Reflexão sobre ETL e qualidade dos dados

ETL significa Extrair, Transformar e Carregar. Neste projeto, a extração ocorreu na leitura do arquivo `varejo.csv` com pandas. A transformação incluiu a correção do separador do arquivo, a remoção de colunas vazias e duplicatas, a conversão da coluna de data e a padronização de categorias não informadas. Por fim, a base tratada foi carregada no arquivo `df_limpo.csv`.

A qualidade dos dados é importante porque informações incorretas, repetidas ou incompletas podem gerar conclusões equivocadas. Nesta análise, as duplicatas poderiam aumentar artificialmente a quantidade de itens e compras. Além disso, a categoria `#N/D` não permitia identificar corretamente alguns produtos. Por isso, os problemas encontrados foram tratados e documentados antes da geração das estatísticas e dos agrupamentos.

Mesmo após a limpeza, a base possui limitações, como a ausência de preço e valor de venda. Isso mostra que tratar dados melhora a análise, mas não cria informações que não existem na fonte original.

## Como executar o projeto

1. Clone o repositório:

```powershell
git clone https://github.com/mateusaimi/Miniprojeto_Mateus_Aimi_Analise_de_Dados_T4.git
```

2. Entre na pasta do projeto:

```powershell
cd Miniprojeto_Mateus_Aimi_Analise_de_Dados_T4
```

3. Baixe o arquivo `varejo.csv` no Kaggle e coloque-o na pasta do projeto.

4. Instale o pandas, caso necessário:

```powershell
py -m pip install pandas
```

5. Execute o script:

```powershell
py miniprojeto_varejo.py
```

Ao final, o script exibirá os resultados da análise no terminal e gerará o arquivo `df_limpo.csv`.
