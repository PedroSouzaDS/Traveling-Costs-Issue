# Análise exploratória problema de passagens aéreas
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelBinarizer
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import iplot
import chart_studio.plotly as cpy

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
# Inclui coluna alta/baixa temporada binário (correlation)
df['Temporada_bin']=LabelBinarizer().fit_transform(df.Temporada)
# Analise de Correlacoes
df.corr()
sns.pairplot(df)
# Analise de medidas de tendencia central e boxplot, boxplot sem valores "zero"
df_fig = df.melt(id_vars = ['Orgao_Solicitante','Nome_viajante','Data_Solicitacao','Data_Inicio','Ano','Intervalo',
                            'Temporada','Temporada_bin'])
df_fig.columns = ['Orgao_Solicitante','Nome_viajante','Data_Solicitacao','Data_Inicio','Ano',
                  'Intervalo','Temporada','Temporada_bin','Despesa','Valor']

df_fig = df_fig[df_fig.Valor != 0]

boxplot = px.box(df_fig, x='Despesa', y='Valor', title='Gastos Totais')
boxplot.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot)

boxplot17 = px.box(df_fig, x=df_fig.Despesa[df_fig.Ano == '2017'], 
                   y=df_fig.Valor[df_fig.Ano == '2017'], title = 'Gastos 2017')
boxplot17.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot17)

boxplot18 = px.box(df_fig, x=df_fig.Despesa[df_fig.Ano == '2018'], 
                   y=df_fig.Valor[df_fig.Ano == '2018'], title = 'Gastos 2018')
boxplot18.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot18)

boxplot19 = px.box(df_fig, x=df_fig.Despesa[df_fig.Ano == '2019'], 
                   y=df_fig.Valor[df_fig.Ano == '2019'], title = 'Gastos 2019')
boxplot19.update_traces(quartilemethod = 'exclusive')
cpy.iplot(boxplot19)

# Pizza (sumburst: hierarquico)
snb = px.sunburst(df, path = ['Orgao_Solicitante', 'Nome_viajante'], values = 'Vr_Viagem')
snb.update_traces(textinfo = 'label+percent entry')
cpy.iplot(snb)

snbYear = px.sunburst(df, path = ['Ano', 'Orgao_Solicitante', 'Nome_viajante'], values = 'Vr_Viagem')
snbYear.update_traces(textinfo = 'label+percent entry')
cpy.iplot(snbYear)

# Um Dashboard apenas com Analise de boxplot
# Outro Dashboard com Sumburst, ARIMA, Linhas
# Fazer no Matplotlib e colocar só no relatório o Pareto
 