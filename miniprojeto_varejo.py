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

# --- Validação do perfil dos clientes ---

# Verifica quantos valores diferentes cada cliente possui em seus dados
perfil_clientes = df.groupby("CL_ID").agg(
    filhos_distintos=("CL_FHL", "nunique"),
    generos_distintos=("CL_GENERO", "nunique"),
    segmentos_distintos=("CL_SEG", "nunique")
)

print("\n--- Validação do perfil por cliente ---")
print("Quantidade de clientes únicos:", perfil_clientes.shape[0])
print(
    "Clientes com mais de um número de filhos:",
    (perfil_clientes["filhos_distintos"] > 1).sum()
)
print(
    "Clientes com mais de um gênero:",
    (perfil_clientes["generos_distintos"] > 1).sum()
)
print(
    "Clientes com mais de um segmento:",
    (perfil_clientes["segmentos_distintos"] > 1).sum()
)

# --- Estatísticas descritivas: número de filhos por cliente ---

# Como o perfil foi validado, mantém uma única linha para cada cliente
clientes = df.drop_duplicates(subset="CL_ID").copy()
filhos = clientes["CL_FHL"]

print("\n--- Estatísticas do número de filhos por cliente ---")
print("Contagem de clientes:", filhos.count())
print("Média:", round(filhos.mean(), 2))
print("Mediana:", filhos.median())
print("Desvio padrão:", round(filhos.std(), 2))
print("Moda(s):", filhos.mode().tolist())
print("Mínimo:", filhos.min())
print("Máximo:", filhos.max())

print("\nQuartis:")
print(filhos.quantile([0.25, 0.50, 0.75]))

print("\nDistribuição do número de filhos por cliente:")
print(filhos.value_counts().sort_index())

# --- Validação do identificador de compra ---

# Agrupa os registros pelo identificador da compra
resumo_compras = df.groupby("CO_ID").agg(
    datas_diferentes=("DATA", "nunique"),
    clientes_diferentes=("CL_ID", "nunique"),
    itens_registrados=("PR_ID", "size")
)

# Verifica se um mesmo código de compra aparece para mais de uma data ou cliente
compras_com_datas_diferentes = (resumo_compras["datas_diferentes"] > 1).sum()
compras_com_clientes_diferentes = (resumo_compras["clientes_diferentes"] > 1).sum()

print("\n--- Validação de CO_ID ---")
print("Quantidade de CO_ID diferentes:", resumo_compras.shape[0])
print("CO_ID ligados a mais de uma data:", compras_com_datas_diferentes)
print("CO_ID ligados a mais de um cliente:", compras_com_clientes_diferentes)

print("\nQuantidade de itens por compra:")
print(resumo_compras["itens_registrados"].describe())

# --- Agrupamentos para identificar padrões ---

# Agrupamento 1: compras por gênero e segmento do cliente
compras_por_genero_segmento = df.groupby(
    ["CL_GENERO", "CL_SEG"]
).agg(
    compras_unicas=("CO_ID", "nunique"),
    clientes_unicos=("CL_ID", "nunique"),
    itens_registrados=("PR_ID", "size")
).sort_values("compras_unicas", ascending=False)

compras_por_genero_segmento["percentual_compras"] = (
    compras_por_genero_segmento["compras_unicas"]
    / compras_por_genero_segmento["compras_unicas"].sum() * 100
).round(2)

print("\n--- Agrupamento 1: compras por gênero e segmento ---")
print(compras_por_genero_segmento)

# Agrupamento 2: itens e compras por categoria de produto
itens_por_categoria = df.groupby("PR_CAT").agg(
    itens_registrados=("PR_ID", "size"),
    produtos_distintos=("PR_ID", "nunique"),
    compras_unicas=("CO_ID", "nunique")
).sort_values("itens_registrados", ascending=False)

print("\n--- Agrupamento 2: itens por categoria ---")
print(itens_por_categoria)