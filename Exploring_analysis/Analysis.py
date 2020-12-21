# Análise exploratória problema de passagens aéreas
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelBinarizer
import plotly.express as px
import chart_studio.plotly as cpy
from datetime import datetime
import matplotlib.pyplot as plt

import chart_studio
chart_studio.tools.set_credentials_file(username='psouza.neto', api_key='Dwe3WEaa8deqj6bIgLMu')

df = pd.read_excel('C:/Users/Pedro Fernandes/Desktop/Github/Traveling-Costs-Issue/Exploring_analysis/Custos_passagem_diárias(corrigido).xlsx')
# Elimina NUmero_PCDP
df.drop('Numero_PCDP', axis=1, inplace=True)
# Coluna Ano
df['Ano'] = df.Data_Solicitacao.dt.year
df['Ano'] = df.Ano.astype(str)
# Inclui coluna dif data de embarque
df['Intervalo'] = abs(df.Data_Inicio - df.Data_Solicitacao) #abs impede negativos
df.Intervalo = df.Intervalo.dt.days.astype('int16')
# Inclui coluna alta/baixa temporada da data da Solicitacao/reserva
# Datas de alta temporada: Mês 12, 01, 02, 07 e vésperas de feriados 10/04, 21/04, 01/05, 11/06, 02/11, 15/11
df['Temporada'] = np.NAN
pos = 0
while pos < len(df.Data_Solicitacao):
    if df.Data_Solicitacao[pos].month in [1,2,7,12]:
        df.Temporada[pos] = 'Alta'
    else: 
        df.Temporada[pos] = 'Baixa'
    pos+=1
df['Temporada_bin']=LabelBinarizer().fit_transform(df.Temporada)
df_fig = df.melt(id_vars = ['Orgao_Solicitante','Nome_viajante','Data_Solicitacao','Data_Inicio','Ano','Intervalo',
                            'Temporada','Temporada_bin'], value_vars=['Vr_Diaria', 'Vr_Passagem', 'Vr_Viagem'])
df_fig.columns = ['Orgao_Solicitante','Nome_viajante','Data_Solicitacao','Data_Inicio','Ano',
                  'Intervalo','Temporada','Temporada_bin','Despesa','Valor']
df_fig = df_fig[df_fig.Valor != 0]

# Perguntas de negócio
# 1 - Quais os gastos anuais de 2017, 2018, 2019 e Totais tanto com passagens qto com diarias?
# 2017
print('GASTOS EM 2017')
print('Total gasto em DIÁRIAS em 2017: R$','%.2f' % (df.Vr_Diaria[df.Ano == '2017'].sum()))
print('Total gasto em PASSAGENS em 2017: R$','%.2f' % (df.Vr_Passagem[df.Ano == '2017'].sum())) 
print('Total gasto em VIAGENS (DIÁRIA + PASSAGEM) em 2017: R$','%.2f' % (df.Vr_Viagem[df.Ano == '2017'].sum())) 
# 2018
print('GASTOS EM 2018')
print('Total gasto em DIÁRIAS em 2018: R$','%.2f' % (df.Vr_Diaria[df.Ano == '2018'].sum()))
print('Total gasto em PASSAGENS em 2018: R$','%.2f' % (df.Vr_Passagem[df.Ano == '2018'].sum())) 
print('Total gasto em VIAGENS (DIÁRIA + PASSAGEM) em 2018: R$','%.2f' % (df.Vr_Viagem[df.Ano == '2018'].sum())) 
# 2019
print('GASTOS EM 2019')
print('Total gasto em DIÁRIAS em 2019: R$','%.2f' % (df.Vr_Diaria[df.Ano == '2019'].sum()))
print('Total gasto em PASSAGENS em 2019: R$','%.2f' % (df.Vr_Passagem[df.Ano == '2019'].sum())) 
print('Total gasto em VIAGENS (DIÁRIA + PASSAGEM) em 2019: R$','%.2f' % (df.Vr_Viagem[df.Ano == '2019'].sum()))
# Total 3 anos
print('GASTOS TOTAIS DOS 3 ANOS')
print('Total gasto DIÁRIA: R$','%.2f' % (df.Vr_Diaria.sum())) 
print('Total gasto PASSAGESNS: R$','%.2f' % (df.Vr_Passagem.sum()))
print('Total gasto VIAGENS (DIÁRIA + PASSAGEM): R$','%.2f' % (df.Vr_Viagem.sum()))
# 2Faca uma nálise de boxplot?
# a)  Qual o comportamento dos gráficos em relação a assimetria suas assimetrias?
# b)  Qual o Desvio Padrão entre estes valores?   
# c)  Há outliers entre os dados de ambas as despesas? Fazer uma análise de Outliers.
# d)  Quais informações os boxplot podem agregar na solução do problema do negócio? Quais mudanças
# podem ser sugeridas por conta desta visualização?
boxplot = px.box(df_fig, y='Valor', title='Gastos Totais', color='Despesa' )
boxplot.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot)

boxplot17 = px.box(df_fig, y=df_fig.Valor[df_fig.Ano == '2017'], title = 'Gastos 2017',
                   color=df_fig.Despesa[df_fig.Ano == '2017'])
boxplot17.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot17)

boxplot18 = px.box(df_fig, y=df_fig.Valor[df_fig.Ano == '2018'], title = 'Gastos 2018',
                   color=df_fig.Despesa[df_fig.Ano == '2018'])
boxplot18.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot18)

boxplot19 = px.box(df_fig, y=df_fig.Valor[df_fig.Ano == '2019'], title = 'Gastos 2019',
                   color=df_fig.Despesa[df_fig.Ano == '2019'])
boxplot19.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot19)
# 3.  Há algum tipo de correlação entre os dados?  
df.corr()
sns.pairplot(df) 
# 4.  Qual departamento lidera as solicitações de viagens? 
# Deste departamento qual o professor com mais solicitações e gastos? 
snb = px.sunburst(df, path = ['Orgao_Solicitante', 'Nome_viajante'], values = 'Vr_Viagem')
snb.update_traces(textinfo = 'label+percent entry')
cpy.iplot(snb)

snbYear = px.sunburst(df, path = ['Ano', 'Orgao_Solicitante', 'Nome_viajante'], values = 'Vr_Viagem')
snbYear.update_traces(textinfo = 'label+percent entry')
cpy.iplot(snbYear)   
# 5.  Qual Órgão da UFOP lidera as solicitações de viagens? 
# Deste Órgão qual o servidor com mais solicitações e gastos?    
# 6.  Com base nas despesas destes anos fazer uma previsão 
# destes gastos para o ano de para os próximos anos 2020, 2021 e 2022 com ARIMA. 
# Separa dados Times Series
data = df.Data_Solicitacao # Já se encontra em "datetime"
valor = df.Vr_Viagem
ts = pd.concat([data, valor], axis = 1)
ts.set_index('Data_Solicitacao', inplace = True)
ts.info()

# 7.  Há alguma relação de Pareto entre as despesas e solicitantes? 
# Fazer no Matplotlib e colocar só no relatório o Pareto
 