import pandas as pd

# Carrega a base de dados para uma tabela chamada df
df = pd.read_csv("varejo.csv", sep=";")
df = df.dropna(axis=1, how="all")

# Mostra informações iniciais sobre a base
print("Número de registros:", len(df))
print("\nNomes das colunas:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)

print("\nPrimeiras 5 linhas:")
print(df.head())

print("\nValores nulos por coluna:")
print(df.isnull().sum())

print("\nQuantidade de linhas duplicadas:")
print(df.duplicated().sum())

# Investiga as linhas duplicadas antes de decidir se serão removidas
linhas_duplicadas = df[df.duplicated(keep=False)]

print("\nLinhas envolvidas em duplicações:")
print(len(linhas_duplicadas))

print("\nExemplo de linhas duplicadas:")
print(linhas_duplicadas.head(10).to_string(index=False))

# Verifica se todas as datas podem ser interpretadas corretamente
datas_teste = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")

print("\nQuantidade de datas inválidas:")
print(datas_teste.isna().sum())

print("\nPeríodo presente na base:")
print("Data mais antiga:", datas_teste.min())
print("Data mais recente:", datas_teste.max())

# Procura textos vazios nas colunas mais importantes
colunas_texto = ["CL_GENERO", "CL_SEG", "PR_CAT", "PR_NOME"]

for coluna in colunas_texto:
    quantidade_vazia = df[coluna].str.strip().eq("").sum()
    print(f"\nTextos vazios em {coluna}: {quantidade_vazia}")

# Mostra os valores existentes nas colunas categóricas principais
print("\nValores de CL_GENERO:")
print(df["CL_GENERO"].value_counts())

print("\nValores de CL_SEG:")
print(df["CL_SEG"].value_counts())

print("\nValores de PR_CAT:")
print(df["PR_CAT"].value_counts())