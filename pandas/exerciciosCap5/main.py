import pandas as pd
file_path = '/home/joao/Workspace/Inatel 2024/C111-Analise-de-Dados/pandas/exerciciosCap5/paises.csv'

print('\n------- 1 -------')
print('------- A -------')
df = pd.read_csv(file_path, delimiter=';')
print(df['Country'][df['Region'] == 'OCEANIA                            '])

print('\n------- B -------')
print((df['Region'] == 'OCEANIA                            ').sum(),
      "países da Oceania")

print('\n------- 2 -------')
print("Afabetização", df['Literacy (%)'].mean(), "%")

print('\n------- 3 -------')
max_population_index = df['Population'].idxmax()
print(df.loc[max_population_index, ['Country', 'Region']])

print('\n------- 4 -------')
paises_sem_costa_maritima = df['Country'][df['Coastline (coast/area ratio)'] ==
     0]
paises_sem_costa_maritima.to_csv('paises_sem_costa.csv', index=False)
print(paises_sem_costa_maritima)
