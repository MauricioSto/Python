# comando para renomear
red_df = red_df.rename(columns = {'total_sulfur-dioxide':'total_sulfur_dioxide'}) 
or
df_08.rename(columns={'Sales Area':'Cert Region'}, inplace=True)

# crie vetor de cor para o dataframe tinto
color_red = np.repeat('red', 1599)

# anexe dataframes
wine_df = white_df.append(red_df, ignore_index=True)

# exiba o dataframe para ver se tudo deu certo
wine_df.head()

# salvando datasets
wine_df.to_csv('winequality_edited.csv', index=False)

# gerando informações sobre o dataframe
wine_df.info()

# isto retorna as primeiras linhas do nosso dataframe
# como padrão, retorna as primeiras cinco linhas
df.head()

# embora você possa especificar quantas linhas você gostaria que fossem retornadas
df.head(20)

# isso também se aplicar ao comando `.tail()` que retorna as últimas linhas do dataframe
df.tail(2)

# retorna a quantidade de valores duplicados no dataframe
sum(df.duplicated())

# elimine dados duplicados
df.drop_duplicates(inplace = True)

#retorna valores unicos no dataframe
df.nunique()

# isto retorna estatísticas descritivas úteis para cada coluna de dados
df.describe()

#contar numero de linhas em branco
df_all_08.isnull().sum()

#seta tipos de informações numa determinada dataframe com determinada coluna
set(df_all_08['Fuel'])

# isto retorna uma tupla com as mesmas dimensões do dataframe
df.shape

# isto retorna os tipos de dados das colunas
df.dtypes

# Exibir o índice e rótulo de cada coluna
for i, v in enumerate(df.columns):
    print(i, v)
	
# descarte colunas do conjunto de dados 
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)

# substitua espaços por rótulos com subtrações e letras minúsculas para o conjunto de dados
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# use médias para preencher valores ausentes
mean = df['smoothness_mean'].mean()
df['smoothness_mean'].fillna(mean,inplace=True)

# remova "_mean" dos nomes das colunas conceito para tirar os ultimos caracteres
new_labels = []
for col in df.columns:
    if '_mean' in col:
        new_labels.append(col[:-5])  # exclua os últimos 6 caracteres
    else:
        new_labels.append(col)

# atribua novos rótulos às colunas do dataframe
df.columns = new_labels

# Encontre a qualidade média de cada tipo de vinho (tinto e branco) com groupby
df.groupby(['quality','color']).mean()

# Encontre a qualidade média de cada nível de acidez com groupby
df.groupby(['acidity_levels', 'quality'],as_index=False)['fixed_acidity'].mean()

# selecione amostras com teor alcóolico abaixo da mediana
m = df['alcohol'].mean()
low_alcohol = df.query('alcohol < @m')

# selecione amostras com teor alcóolico maior ou igual à mediana
high_alcohol = df.query('alcohol > @m')

#grafico de histograma
wine_df['fixed_acidity'].plot(kind='hist');

#grafico de dispersão
wine_df.plot(x ='quality', y ='volatile_acidity', kind ='scatter');

# tente usar as funções  astype do Pandas para converter a coluna
# air_pollution_score do conjunto de dados de 2008 para float 
df_08['air_pollution_score'] = df_08['air_pollution_score'].astype(float)

# converta a coluna de poluição do ar de 2018 de int to float
df_18['air_pollution_score'] = df_18['air_pollution_score'].astype(int)

# Extraia int de strings da coluna cyl de 2008
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)

## processo para dividir em dois os dados em uma coluna com dois valores:
# Primeiro, vamos obter todos os híbridos de 2008
hb_08 = df_08[df_08['fuel'].str.contains('/')]
# crie duas cópias do dataframe com híbridos de 2008
df1 = hb_08.copy()  # data on first fuel type of each hybrid vehicle
df2 = hb_08.copy()  # data on second fuel type of each hybrid vehicle
# colunas que devem ser divididas por "/"
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg', 'greenhouse_gas_score']

# aplique a função split para cada coluna de cada cópia do dataframe
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])
# combine dataframes para adicionar ao dataframe original
new_rows = df1.append(df2)

# agora temos linhas separadas para cada tipo de combustível de cada veículo!
new_rows
# descarte as linhas originais que continham híbridos
df_08.drop(hb_08.index, inplace=True)

# adicione as novas linhas separadas
df_08 = df_08.append(new_rows, ignore_index=True)

# verifique se todas linhas originais com híbridos, que continham "/"s, sumiram
df_08[df_08['fuel'].str.contains('/')]

# verifique a contagem de valores para a coluna cyl de 2008
df_08['cyl'].value_counts()

# trace as barrass
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# título e rótulos
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # localização dos marcadores no eixo x
labels = ['3', '4', '5', '6', '7', '8', '9']  # rótulos dos marcadores no eixo x
plt.xticks(locations, labels)

# legenda
plt.legend()

# descarte linhas com quaisquer valores nulos em ambos conjuntos de dados
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)

# trace um gráfico de caixas para cada variável
df_powerplant['AT'].plot(kind='box');