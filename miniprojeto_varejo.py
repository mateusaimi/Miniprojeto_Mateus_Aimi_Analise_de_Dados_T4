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

# --- Limpeza dos dados ---

# Guarda a quantidade de linhas antes da limpeza
linhas_antes = len(df)

# Conta e remove linhas totalmente duplicadas
duplicatas_removidas = df.duplicated().sum()
df = df.drop_duplicates().copy()

# Converte a coluna de data para o tipo datetime
df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")

# Remove espaços desnecessários nas categorias
df["PR_CAT"] = df["PR_CAT"].str.strip()

# Verifica se existem categorias vazias
categorias_vazias = df["PR_CAT"].eq("").sum()

if categorias_vazias > 0:
    df.loc[df["PR_CAT"].eq(""), "PR_CAT"] = "Sem Categoria"
    print(f"\nCategorias vazias substituídas: {categorias_vazias}")
else:
    print("\nNão foram encontradas categorias vazias.")

# Trata #N/D como categoria não informada
categorias_nao_informadas = df["PR_CAT"].eq("#N/D").sum()
df.loc[df["PR_CAT"].eq("#N/D"), "PR_CAT"] = "Sem Categoria"

# Mostra o resultado da limpeza
print("\n--- Resultado da limpeza ---")
print("Linhas antes da limpeza:", linhas_antes)
print("Duplicatas removidas:", duplicatas_removidas)
print("Linhas após a limpeza:", len(df))
print("Categorias #N/D substituídas:", categorias_nao_informadas)
print("Tipo da coluna DATA após conversão:", df["DATA"].dtype)
print("\nValores de PR_CAT após limpeza:")
print(df["PR_CAT"].value_counts())