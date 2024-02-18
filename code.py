import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados
data = {
    'dia': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'venda': [5.11, 4.99, 5.02, 5.21, 5.07, 5.09, 5.13, 5.12, 4.94, 5.03]
}

df = pd.DataFrame(data)

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
line_plot = sns.lineplot(x='dia', y='venda',marker='o', data=df)
line_plot.set(title='Preço da Gasolina ao Longo dos Dias', xlabel='Dia', ylabel='Preço de Venda')

# Salvando o gráfico como gasolina.png
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()