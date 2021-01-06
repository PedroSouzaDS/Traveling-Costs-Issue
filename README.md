## Problema com passagens e diárias de viagens para assuntos acadêmicos e administrativos da Universidade Federal de Ouro Preto

A Universidade Federal de Ouro Preto-UFOP, localizada na cidade de Ouro Preto-MG, Brasil, tem uma grande demanda por passagens, tanto aéreas quanto terrestres, e de diárias para hotéis e pousadas em outras localidades devido a compromissos tanto acadêmicos quanto administrativos ou até mesmo políticos, tais demandas são de responsabilidade da PROPLAD (Pró-Reitoria de Orçamento, Planejamento e Administração). 

![aviao](https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/aviao.gif)

No entanto, de acordo com o setor  de Compras da extinta fundação de apoio da Universidade, a FEOP, estes custos poderiam ser otimizados pois, segundo o setor, acontece um certo desperdício devido à falta de planejamento da viagem (compra de passagens na última hora) ou até mesmo a própria exigência do solicitante muitas vezes desnecessárias. Tais custos com viagens e diárias nos últimos três anos (2017, 2018 e 2019) totalizaram, segundo os dados do problema, em R$2.270.704,55.

A Proposta do estudo é analisar dados destes custos e gerar insights a respeito, fazer análises preditivas para os gastos no futuro com o intuito de oferecer um suporte ao tomador de decisões do órgão competente tanto para que possa buscar alternativas mais viáveis economicamente quanto propor melhorias dentro do próprio órgão.

ESTE PROBLEMA FOI SOLUCIONADO EM DUAS ETAPAS:

I - LIMPEZA DOS DADOS NA PASTA "Data Cleaning", ONDE É APRESENTADO DETALHES DE TODA A ETAPA DE PRÉ-PROCESSAMENTO COMO AS TRANSFORMAÇÃO E PREPARAÇÕES DOS DADOS. O PASSO A PASSO DA RESOLUÇÃO DESTA PARTE PODE SER CONSULTADA NO PRÓPRIO ARQUIVO JUPYTER NOTEBOOK: 
https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Data%20Cleaning/Data_Cleaning.ipynb

II - AS SEGUINTES PERGUNTAS RELACIONADAS AOS PROBLEMAS DO NEGÓCIO SERÃO RESPONDIDAS AO LONGO DA ANÁLISE EXPLORATÓRIA TAMBÉM NO PRÓPRIO ARQUIVO JUPYTER NOTEBOOK:
https://github.com/PedroSouzaDS/Traveling-Costs-Issue/blob/main/Exploring_analysis/An%C3%A1lise_exploratoria.ipynb


PRINCIPAIS PROBLEMAS:
1.  Sobre os gastos:

a) Qual órgão demandou o maior gasto em 2017? Qual o solicitante desse órgão foi o maior responsável pelo gasto?

b) E em 2018?

c) E em 2019?

2.  Qual o tipo mais solicitado, diárias ou passagens? Qual dos dois demandou os maiores gastos e quanto?

3.  Fazer uma análise de boxplot para cada ano e para o total de solicitações:

a) Analisar e fazer uma comparação dos outliers de cada ano e discorrer sobre.

b) Analisar os limites inferiores e superiores discorrer sobre.

c) Analisar as assimetrias discorrer sobre.

d) Comparar o comportamento destes parâmetros dos anos individuais com os parâmetros do gráfico do total (Valor Viagem) discorrer sobre. 
    
4.  Qual o desvio padrão para cada ano? Comparar os desvios padrão de cada entre si e entre o total.
    
5.  Há correlação entre os dados? Quais são as correlações?
    
6.  Fazer uma análise de Time Series. 
    
7.  Fazer uma previsão de futuras demandas usando ARIMA, para 2020, 2021, 2022 e 2023? 

8. Há relação de Pareto entre os dados? Fazer um gráfico de Pareto e analisar.
