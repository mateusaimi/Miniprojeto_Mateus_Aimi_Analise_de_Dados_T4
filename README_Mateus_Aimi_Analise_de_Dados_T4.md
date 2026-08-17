# Instruções de execução

## Requisitos

- Python 3 instalado.
- Biblioteca pandas instalada.
- Arquivo `varejo.csv` na mesma pasta do script.

## Como executar

1. Abra a pasta do projeto no VS Code.
2. Abra o terminal integrado.
3. Caso o pandas não esteja instalado, execute:

```powershell
py -m pip install pandas
```

4. Execute o script:

```powershell
py miniprojeto_varejo.py
```

5. O terminal exibirá as informações da análise, as estatísticas, os agrupamentos e as conclusões.
6. Ao final da execução, será criado o arquivo `df_limpo.csv` com os dados tratados.

## Arquivos principais

- `miniprojeto_varejo.py`: código da análise.
- `varejo.csv`: base original.
- `df_limpo.csv`: base após a limpeza.