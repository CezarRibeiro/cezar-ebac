import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Substituindo os dados
data = pd.read_csv('gasolina.csv')
    


df = pd.DataFrame(data)

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
line_plot = sns.lineplot(x='dia', y='venda', marker='o', data=df)
line_plot.set(title='Preço médio da Gasolina na cidade de São Paulo', xlabel='Dia', ylabel='Preço de Venda')

# Salvando o gráfico como gasolina.png
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()